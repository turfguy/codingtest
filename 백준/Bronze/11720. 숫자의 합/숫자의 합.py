n = int(input())
num = int(input())
number = list(map(int,str(num)))

count = 0
for i in number:
        count += i

print (count)