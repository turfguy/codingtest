s = list(map(str,(input())))
strs = []
for char in s:
    if char.isalnum():
        strs.append(char.lower())
count = 0
while len(strs)>1:
    if strs.pop(0) != strs.pop():
        print('False')
        count+=1
if count == 0 :
    print('True')