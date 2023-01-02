pieces = [sum(map(int, exp.split('+'))) for exp in input().split('-')]
print(pieces.pop(0) - sum(pieces))