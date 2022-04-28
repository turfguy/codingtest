counts = int(input())
str = []
for count in range(counts):
    nums,words= list((input().split()))
    array=[]
    for word in words:
        array.append(word)

    result = []
    for arr in array:
            for num in range (int(nums)):
               result.append(arr)

    str.append(''.join(result))

for s in str:
    print(s)