while True:
    x,y = map(int,input().split())
    if(x==0 and y==0):break;
    print('Yes' if x > y else 'No')