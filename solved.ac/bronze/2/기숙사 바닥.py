def sol(R,B):
    for L in range(3,int((R+B)/2)+1):
        for W in range(3,L+1):
            if 2*L + 2*W - 4 == R and L*W == R + B:
                return(L,W)

R,B = map(int,input().split())
print(*sol(R,B))