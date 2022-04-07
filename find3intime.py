# 예제 4-2 시각 (구현)
# 00시00분00초 ~ N시 59분 59초 까지 3이 하나라도 포함되는 경우의 수 구하기
# 입력으로 N 을 받는다.
# 처음에는 N을 입력 받은뒤 시간과 분을 각각 0~59까지의 배열로 선언=> 3중 for문으로 했는데 그럴 필요가 없었다..
# 그냥 시+분+초 를 문자열로 묶어서 조건문 if '3' in 으로 확인하면 됐던건데..

N = int(input())

# time = [i for i in range(0,N+1)],[i for i in range(60)], [i for i in range(60)]
count = 0

for hour in range(N+1):
    for min in range(60):
      for sec in range(60):

          if '3' in str(hour)+str(min)+str(sec): count+=1

print(count)