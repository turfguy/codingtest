import sys
n = int(sys.stdin.readline())
locs = []
locs= set(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
checks = []
checks= list(map(int,sys.stdin.readline().split()))

for check in checks:
    if check in locs:
        print('1')
    else:
        print('0')