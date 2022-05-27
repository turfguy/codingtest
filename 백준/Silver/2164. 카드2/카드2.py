import sys
from sys import stdin
from collections import deque

N = int(sys.stdin.readline())
L = deque([i for i in range(1,N+1)])

while(len(L)>1):
    L.popleft()
    move_num = L.popleft()
    L.append(move_num)

print(L[0])

