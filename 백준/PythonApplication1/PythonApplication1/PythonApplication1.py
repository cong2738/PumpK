n=input()
A = input().split()
n=input()
B = input().split()
for b in B:
    if b in A:
        print(1)
    else:
        print(0)
