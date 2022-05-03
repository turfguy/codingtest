n,m = list(map(int,input().split()))

num1= list(map(int,str(n)))
num2= list(map(int,str(m)))
num1.reverse()
num2.reverse()
n = ''.join(map(str,num1))
m = ''.join(map(str,num2))

if n > m :
    print (n)
else :
    print(m)