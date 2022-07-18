n = int(input())
input_list = []
for i in range(n):
    input_data = input().split()
    input_list.append((input_data[0], int(input_data[1])))

input_list= sorted(input_list, key=lambda stu : stu[1])

for stu in input_list:
    print(stu[0], end = ' ')