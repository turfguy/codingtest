n = int(input())
nums = list(map(int,input().split()))

count = 0

for num in nums:
    wrong = 0 
    if num>1:
        for i in range (2,num):
            if num%i == 0 :
                    wrong+=1

        if wrong == 0:
            count += 1


print(count)