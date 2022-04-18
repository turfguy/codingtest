arr = []

for i in range(999):
    arr.append(int(input()))
    if arr[i] == 0 :
        arr.remove(0)
        break

for word in arr:
        if int(word) == int(str(word)[::-1]) :
            print ('yes')
        else:
            print ('no')