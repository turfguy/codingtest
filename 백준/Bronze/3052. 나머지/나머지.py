num_list = []
for _ in range(10):
    num_list.append(input())

mod = []
count = 0
for num in num_list :
   
    if int(num)%42 not in mod:
            count +=1
            mod.append(int(num)%42)


print(count)