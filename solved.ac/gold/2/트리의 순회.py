import sys
from collections import defaultdict as dd
sys.setrecursionlimit(100000)
readline = sys.stdin.readline

def div(i_s,i_e,p_s,p_e):
    if i_s >= i_e and p_s >= p_e: return
    
    # Find Divide Point N divide    
    for idx in range(i_e-i_s+1):
        if inorder[i_s+idx] == postorder[p_e-1]: 
            preorder.append(postorder[p_e-1])
            div(i_s,i_s+idx,p_s,p_s+idx)
            div(i_s+idx+1,i_e,p_s+idx,p_e-1)
            break
    
n = int(readline())
inorder = list(map(int,readline().split()))
postorder = list(map(int,readline().split()))

preorder = []
div(0,n,0,n)

print(*preorder)