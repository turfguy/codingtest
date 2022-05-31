import sys
import math

A,B,V = map(int,sys.stdin.readline().split())
count = (V-B)/(A-B)
print(math.ceil(count))