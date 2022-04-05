# "1이 될떄까지"  그리디
# 1. n에서 1을 뺀다.
# 2. 1/2 를 수행한다.
# 1번과 2번의 과정을 최소로 수행하여 1을 만드는 최소 횟수 찾기 (입력 예시 25,5 / 출력예시 2)

n,k = map(int,input().split())
result = 0
count = 0

while True:
        if n==1 : break
        elif (n%k)!= 0:
            n -= 1
            count += 1
        else:
            n = n//k
            count += 1

print(count)