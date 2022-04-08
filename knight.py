# 왕실의 나이트 (실전문제)
# 8*8 좌표 평면 체스판에서 임의로 위치를 받은뒤, 나이트 이동가능 경우의 수 찾기
# 나이트의 이동 법칙
# 1. 수평으로 두칸 => 수직 이동 한칸
# 2. 수직으로 두칸 => 수평 이동 한칸

n = ['a','b','c','d','e','f','g','h']
m = [ i+1 for i in  range(8)]
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

loc = input()
rowN,colN= list(loc)
col = int(colN)
row = ( n.index(rowN) + 1)
print(row,col)
count = 0

for step in steps:
        next_row = row + step[0]
        next_col = col + step[1]
        if next_row>=1 and next_row<=8 and next_col>=1 and next_col<=8:
                count+= 1


print(count)