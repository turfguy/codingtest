# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 0.5 초 (추가 시간 없음)	256 MB	44884	24512	20722	56.408%
# 문제
# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
#
# 명령은 총 여덟 가지이다.
#
# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
import sys
from sys import stdin

N = int(sys.stdin.readline())
queue= []

for _ in range(N) :
    insert = sys.stdin.readline().split()
    if (insert[0] == 'push_front'):
        queue.insert(len(queue),insert[1])
    elif (insert[0] == 'push_back'):
        queue.insert(0, insert[1])
    elif (insert[0] == 'pop_front'):
        if len(queue)!=0 :
            print(queue.pop())
        else: print(-1)
    elif (insert[0] == 'pop_back'):
        if len(queue)!=0 :
            print(queue.pop(0))
        else: print(-1)
    elif (insert[0] == 'size'):
        print(len(queue))
    elif (insert[0] == 'empty'):
        if len(queue)==0 :
            print(1)
        else:
            print(0)
    elif (insert[0] == 'front'):
        if len(queue) == 0 :
            print(-1)
        else:
            print(queue[len(queue) -1])
    elif (insert[0] == 'back'):
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])



