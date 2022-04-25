n,m = map(int,input().split())
nums = list(map(int,input().split()))
b= len(nums)

count = 0
for i in range(0, b - 2):
        for j in range(i + 1, b - 1):
                for k in range(j + 1, b):
                        if nums[i] + nums[j] + nums[k] > m:
                                continue
                        else:
                                count = max(count, nums[i] + nums[j] + nums[k])


print(count)