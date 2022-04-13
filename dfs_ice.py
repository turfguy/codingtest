# 음료수 얼려먹기
# n*m 크기 얼음틀 => 구멍이 뚫려있으면 0, 칸막이가 있으면 1로 표시
# 구멍이 뚫린 부분끼리 상하좌우가 붙어있으면 연결된 것으로 간주한다.
# 이때, 얼음 틀의 모양이 주어졌을때 생성되는 총 아이스크림의 개수를 구하는 프로그램
# 입력 조건 : 첫번째 줄에서 세로 길이 n/ 가로 길이 m
#           두번째 줄부터 N+1 번째 줄까지 얼음틀의 형태
# 출력 조건 : 한번에 만들수있는 아이스크림의 개수를 출력한다.

n,m = map(int,input().split())

graph = []
for i in range (n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>= m:
        return False
    if graph[x][y] == 0:
        graph[x][y]= 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result= 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
                result+=1

print (result)