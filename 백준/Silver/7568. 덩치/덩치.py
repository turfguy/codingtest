N = int(input())
slist=[]
for i in range(N):
   weight,height = map(int, input().split())
   slist.append((weight, height))

for i in slist:
    rank = 1
    for j in slist:
        if (i[0]!=j[0]) & (i[1]!=j[1]):
                if(i[0]<j[0])&(i[1]<j[1]):
                    rank+=1
    print(rank)