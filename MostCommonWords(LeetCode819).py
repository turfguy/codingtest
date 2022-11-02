# 가장 흔한 단어 / 리트코드 819번 문제
# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
# 대소문자 구분을 하지 않으며, 구두점(쉼표,마침표 등) 또한 무시한다.
import collections
import re


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
banned = ["hit"]

words = [word for word in re.sub(r'[^\w]',' ',paragraph)
         .lower().split() if word not in banned ]
# 리스트 컴프리헨션을 이용해서 전처리

counts = collections.Counter(words)
print(counts.most_common(1)[0][0])