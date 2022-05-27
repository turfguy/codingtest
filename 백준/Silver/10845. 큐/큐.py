import sys
from sys import stdin

N = int(sys.stdin.readline())
queue = []

for _ in range(N) :
    insert = sys.stdin.readline().split()
    if (insert[0] == 'push'):
        queue.insert(0,insert[1])
    elif (insert[0] == 'pop'):
        if len(queue)!=0 :
            print(queue.pop())
        else: print(-1)
    elif (insert[0] == 'size'):
        print(len(queue))
    elif (insert[0] == 'empty'):
        if len(queue)==0 :
            print(1)
        else:
            print(0)
    elif (insert[0] == 'front'):
        if len(queue) == 0 :
            print(-1)
        else:
            print(queue[len(queue) -1])
    elif (insert[0] == 'back'):
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])



