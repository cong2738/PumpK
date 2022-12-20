for _ in range(int(input())):
    num, *ops = input().split()
    num = float(num)
    for op in ops:
        if op == '@': num *= 3
        elif op == '%': num += 5
        elif op == '#': num -= 7
    print(f'{num:.2f}')