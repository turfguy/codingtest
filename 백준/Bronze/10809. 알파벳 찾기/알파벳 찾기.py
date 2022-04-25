s = input()
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
anum = [-1 for i in range(26)]
slist = list(s)

for i in range(26):
        for ss in slist:
                if alpha[i] in ss:
                        anum[i] = slist.index(alpha[i])


print(*anum)