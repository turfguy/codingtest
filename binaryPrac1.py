def binary(array,target,start,end):
    if start > end :
        return None
    mid = (start+ end) // 2
    if array[mid]== target :
        return mid
    elif array[mid] > target :
        return binary(array,target,start,mid-1)
    else:
        return binary(array,target,mid+1,end)

N = int(input())
pur1 = list(map(int,input().split()))
M = int(input())
pur2 = list(map(int,input().split()))
for p in pur2:
    result = binary(pur1, p, 0, N-1)
    if result!= None:
        print('yes', end= ' ')
    else:
        print('no', end=' ')
