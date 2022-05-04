n,x = map(int,input().split())
num_list= list(map(int,input().split()))
result = []
for num in num_list:
    if int(num) < x:
        result.append(num)

print(*result)