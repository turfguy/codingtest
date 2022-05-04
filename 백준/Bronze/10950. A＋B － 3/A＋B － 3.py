n = int(input())
result = []
for i in range( n ):
    num1,num2 = map(int,input().split())
    result.append(num1+num2)

for res in result:
    print(res)