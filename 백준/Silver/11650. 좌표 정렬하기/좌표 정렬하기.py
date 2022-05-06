import sys
n = int(sys.stdin.readline())
loc = []
for i in range(n):
    loc.append(list(map(int,sys.stdin.readline().split())))
loc.sort(key=lambda x:(x[0],x[1]))
for l in loc:
    print(*l)