#!/usr/bin/env python3
import cgi, os.path
import joblib
import html

# 학습 데이터 읽어 들이기
pklfile = os.path.dirname(__file__) + "/freq.pkl"
clf = joblib.load(pklfile)

# 텍스트 입력 양식 출력하기
def show_form(text, msg=""):
    print("Content-Type: text/html; charset=utf-8")
    print("")
    print("""
        <html><body><form>
        <textarea name="text" rows="8" cols="40">{0}</textarea>
        <p><input type="submit" value="ok"></p>
        <p>{1}</p>
        </form></body></html>
    """.format(html.escape(text), msg))

# 판정하기
def detect_lang(text):
    # 알파벳 출현 빈도 구하기
    text = text.lower() 
    code_a, code_z = (ord("a"), ord("z"))
    cnt = [0 for i in range(26)]

    for ch in text:
        n = ord(ch) - code_a
        if 0 <= n < 26: cnt[n] += 1
    total = sum(cnt)

    if total == 0: return "please enter something"
    freq = list(map(lambda n: n/total, cnt))

    # 언어 예측하기
    res = clf.predict([freq])

    # 언어 코드를 한국어로 변환하기
    lang_dic = {"en":"English","fr":"France",
        "id":"Indonesia", "tl":"Italy"}
    return lang_dic[res[0]]

# 입력 양식의 값 읽어 들이기
form = cgi.FieldStorage()
text = form.getvalue("text", default="")
msg = ""
if text != "":
    lang = detect_lang(text)
    msg = "result :" + lang

# 입력 양식 출력
show_form(text, msg)
