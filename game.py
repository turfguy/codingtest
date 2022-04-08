# 게임개발
# 개임 캐릭터가 맵에서 움직이는 시스템 구현
# 맵의 각칸: (A,B)
# 조건-
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽방향 (반시계로 90도) 부터 차례대로 갈 곳을 정한다.
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지않은 칸이 존재한다면, 왼쪽 방향으로 한칸 전진.
# 그러나, 왼쪽 방향에 가보지 않은 칸이 없다면 회전만 하고 1단계로 돌아간다.
# 3. 만약 네방향이 모두 가본 칸이거나, 바다인 경우 바라보는 방향을 유지한채로 한칸 뒤로 가고 1단계로 돌아간다.
# 하지만, 그 뒤칸이 바다인 경우에는 움직임을 멈춤.
# 입력=>
# n*m 맵의 칸 수를 입력 => 처음 캐릭터의 좌표와 바라보고 있는 방향 => 각 줄 별로 바다/육지 설정
# 출력 =>
# 첫 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.

n, m = map(int,input().split()) # 맵 크기 입력받기
d = [[0]* m for _ in range(n)] #  n*m으로 캐릭터가 들린곳 초기화
x, y, direction = map(int,input().split())
d[x][y]= 1


array = []
for i in range (n):
    array.append(list(map(int,input().split())))

dx= [-1,0,1,0]
dy =[0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x+dx[direction]
    ny = y+dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0 :
        d[nx][ny] = 1
        x= nx
        y= ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4 :
        nx =  x- dx[direction]
        ny =  y- dy[direction]
        if array[nx][ny] == 0 :
            x = nx
            y = ny
        else :
            break
        turn_time = 0



print(count)