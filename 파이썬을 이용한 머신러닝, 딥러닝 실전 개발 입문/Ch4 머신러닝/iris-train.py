from sklearn import svm, metrics
import random, re

# 붓꽃의 CSV 데이터 읽어 들이기
csv = []
with open('iris.csv', 'r', encoding='utf-8') as fp:
    for line in fp:
        line = line.strip()     # 줄바꿈 제거
        cols = line.split(',')  # 쉼표로 자르기
        # 문자열 데이터를 숫자로 변환하기
        fn = lambda n : float(n) if re.match(r'^[0-9\.]+$', n) else n
        cols = list(map(fn, cols))
        csv.append(cols)

# 가장 앞 줄의 헤더 제거
del csv[0]

# 데이터 셔플
random.shuffle(csv)

# 학습 전용 데이터와 테스트 전용 데이터 분할하기(100개, 50개)
total_len = len(csv)
train_len = int(total_len * 0.8)
train_data = []
train_label = []
test_data = []
test_label = []

for i in range(total_len):
    data = csv[i][0:4]
    label = csv[i][4]

    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)
    
# 데이터를 학습시키기
clf = svm.SVC()
clf.fit(train_data, train_label)

# 예측하기
pre = clf.predict(test_data)

# 정답률 구하기
ac_score = metrics.accuracy_score(test_label, pre)
print("정답률 :", ac_score)
