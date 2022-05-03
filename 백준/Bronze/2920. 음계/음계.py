number= list(map(int,input().split()))
nums = [i%8 for i in number]
if nums == [1,2,3,4,5,6,7,0]:
    print('ascending')
elif nums == [0,7,6,5,4,3,2,1]:
    print('descending')
else:
    print('mixed')
