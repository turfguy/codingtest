x,y,w,h = map(int,input().split())
count = [(x-0),(y-0),(w-x),(h-y)]

print(min(count))
