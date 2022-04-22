TF = []

while True:
    n, m, k = map(int, input().split())

    if n==0 and m==0 and k==0 :
            break
    else:
        if ((n*n)+(m*m)) == (k*k) or ((k*k)+(m*m)) == (n*n) or ((n*n)+(k*k)) == (m*m):
                TF.append('right')
        else:
                TF.append('wrong')



for i in TF:
    print(i)