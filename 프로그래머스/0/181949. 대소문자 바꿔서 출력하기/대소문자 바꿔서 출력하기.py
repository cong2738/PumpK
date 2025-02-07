str = input()
res = ""
for c in str:
    if c.isupper():
        res += c.lower()
    else:
        res += c.upper()
print(res)