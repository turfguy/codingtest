n = int(input())
input_list = []
for i in  range (n):
        input_list.append(int(input()))

ans = sorted(input_list, reverse=True)

for a in ans:
    print(a, end=' ')