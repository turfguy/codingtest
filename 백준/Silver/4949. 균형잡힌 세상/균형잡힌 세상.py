while True :
        text = input()
        stack = []
        if text == '.':
                break
        for t in text:
                if t=='(' or t=='[':
                        stack.append(t)
                elif t==']':
                        if len(stack)!=0 and stack[-1]=='[':
                                stack.pop()
                        else:
                                stack.append(t)
                                break
                elif t==')':
                        if len(stack) != 0 and stack[-1] == '(':
                                stack.pop()
                        else:
                                stack.append(t)
                                break

        if len(stack) == 0 :
                print('yes')
        else:
                print('no')