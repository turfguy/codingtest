nums=[]
num = 0
for _ in range(9):
    num= int(input())
    nums.append(num)

maxnum = max(nums)
maxindex = nums.index(maxnum)
print(maxnum)
print(maxindex+1)