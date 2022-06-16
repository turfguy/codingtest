import sys

n = int(sys.stdin.readline())
insert = sorted(list(map(int,sys.stdin.readline().split())))

time = 0
for i in range (n+1):
        for j in range (0,i):
            time+= insert[j]


print(time)