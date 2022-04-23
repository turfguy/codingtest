inte = int(input())
n = inte
count = 0
for i in range(8):
     n= n//10
     count += 1
     if n == 0:
         break

re = (inte - (count*9))


p = 0

for i in range(re,inte):
    answer = i
    if i < 10 :
        answer += i
    else:
        answer+= sum(map(int, str(i)))

    if answer == inte:
                    p = i
                    print(p)
                    break


if p == 0:
    print(p)