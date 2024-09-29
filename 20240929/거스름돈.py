n = int(input())
coin = 0
while n % 5 != 0 and n >= 2:
    n -= 2
    coin += 1
coin = coin + n / 5 if n % 5 == 0 else -1
print(int(coin))