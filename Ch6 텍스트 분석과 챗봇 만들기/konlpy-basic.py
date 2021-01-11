from konlpy.tag import Twitter

twitter = Twitter()
malist = twitter.pos("아버지 가방에 들어가신다.", norm=True, stem=True)
print(malist)

https://ithub.korean.go.kr/user/total/database/corpusManager.do