# n x n 정사각형 지도
# L R U D 으로 움직인다.

n = map(int,input().split())
dirs = input().split()
locX = 1
locY = 1
nx = 0
ny = 0
# 방향이동
move_types = ['L','R','U','D']
dx = [0,0,-1,+1]
dy = [-1,+1,0,0]

for dir in dirs:
    for i in range(len(move_types)):
        if dir == move_types[i]:
            nx = locX + dx[i]
            ny = locY + dy[i]
    if  (nx < 1) or (ny < 1) or (nx > 5) or (ny > 5):
            continue
    locX,locY = nx, ny
print(locX,locY)