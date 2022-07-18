arr = list(map(int,(input().split())))

count_arr = [0 for i in range(101)]
result= []
for ar in arr:
    count_arr[ar] +=1
for count in count_arr:
    if(count!=0 and count!=1):
        result.append(count)
if (len(result)==0):
    result.append(-1)
    print(result)
else: print(result)