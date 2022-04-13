# bfs 구현해보기
# 너비우선탐색 => 가까운 노드부터 탐색하는 알고리즘, fifo 방식인 큐 자료구조로 이용
# 1. 탐색 시작 노드를 큐에 삽입하고 방문처리
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드중에서 방ㅁ누하지 않은 노드를 모두 큐에 삽입하고 방문처리
# 3. (2)번이 불가능할때까지 반복..
# bfs 의 경우 O(N) 의 시간 소요
from collections import  deque

def bfs(graph,start,visited):
    queue = deque([start]) #
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False]*9
bfs(graph,1,visited)