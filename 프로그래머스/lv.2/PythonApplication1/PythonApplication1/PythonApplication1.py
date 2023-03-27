import math

def gg(arr):
    G=arr[0]
    for x in arr:
        G=math.gcd(G,x)
    return G
def ll(arr):
    L=arr[0]
    for x in arr:
        L=math.lcm(L,x)
    return L
def solution(arrayA, arrayB):
    answer=[]
    GA = math.gcd(*arrayA)    
    GB = math.gcd(*arrayB)
    LA = math.lcm(*arrayA)
    LB = math.lcm(*arrayB)
    print(GA,GB)
    if(LA%GB!=0):
        answer.append(GB)
    if(LB%GA!=0):
        answer.append(GA)
    answer.sort(reverse = True)    
    return max(answer)
A=[14, 35, 119]	
B=[18, 30, 102]
print(solution(A,B))
