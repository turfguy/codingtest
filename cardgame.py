# 숫자 카드게임

n,m = list(map(int,input().split()))

result = 0

for i in range(n):
        data = list(map(int,input().split()))
        minval = 10001
        for j in data:
            minval = min(minval,j)

        result = max(result,minval)

print(result)