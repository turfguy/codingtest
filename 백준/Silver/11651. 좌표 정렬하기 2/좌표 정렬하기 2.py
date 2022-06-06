import sys

n = int(sys.stdin.readline())
loc = []
for i in range(n):
        loc.append(list(map(int,sys.stdin.readline().split())))
loc.sort(key=lambda x:((x[1],x[0])))

for l in loc:
        print(l[0],l[1])