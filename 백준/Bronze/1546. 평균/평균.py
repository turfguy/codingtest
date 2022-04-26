n = int(input())
scores = list(map(int,input().split()))
maxscore = max(scores)
result = 0
for score in scores:
   score = score/maxscore*100
   result += score

print(result/n)