n = int(input())
result = []
for i in range(n):
    count = 0
    words = list(map(str,input()))
    stack = 0
    for word in words:
        if word == 'O':
            count+=1
            count+= stack
            stack+=1
        else:
            stack = 0
            continue

    result.append(count)

for c in result:
        print(c)