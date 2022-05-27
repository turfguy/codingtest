N= int(input())
for n in range(N):
    insert= input()
    L = list(insert)
    sum = 0
    for l in L:
        if l == '(':
            sum+=1
        elif l == ')':
            sum-=1
        if sum<0:
            print('NO')
            break
    if sum> 0 :
        print('NO')
    elif sum == 0 :
        print('YES')