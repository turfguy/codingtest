result =[]
while True:
    num1,num2 = map(int,input().split())
    if num1==0 and num2==0 :
        break
    else:
        result.append(num1+num2)

for res in result:
        print(res)
     