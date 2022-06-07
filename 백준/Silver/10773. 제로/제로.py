import sys

n = int(sys.stdin.readline())
list = []
for i in range (n):
        res = int(sys.stdin.readline())
        if res == 0 :
                list.pop()
        else:
                list.append(res)
        res = 0
result = 0
for li in list :
        result+= li
print(result)
