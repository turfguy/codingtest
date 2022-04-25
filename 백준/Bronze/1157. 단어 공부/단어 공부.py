word = input().lower()
wlist = list(set(word))
cnt = []

for i in wlist:
        count = word.count(i)
        cnt.append(count)

if cnt.count(max(cnt))>=2 :
        print('?')
else:
        print(wlist[(cnt.index(max(cnt)))].upper())