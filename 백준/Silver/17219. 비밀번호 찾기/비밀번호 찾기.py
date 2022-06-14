import sys

n, m = map(int, sys.stdin.readline().split())
info = { }
for i in range (n):
            web, pw = sys.stdin.readline().split()
            info[web] = pw


for  j in range (m):
                req = sys.stdin.readline().rstrip()
                print(info[req])