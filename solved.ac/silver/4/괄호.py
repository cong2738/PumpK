for s in [input() for i in range(int(input()))]:
    stack = list()
    for c in s:
        if c == '(':
            stack.append('(')
        elif c == ')':
            try:
                del stack[-1]
            except:
                stack = True
                break
    print('NO' if stack else 'YES')
