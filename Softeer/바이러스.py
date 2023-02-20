#큰수를 작은수로 바꿔줘서 다시연산 시간을 줄인다. 큰수의 연산은 시간이 오래걸린다.
import sys
K,P,N = map(int,sys.stdin.readline().split())
for _ in range(N): 
    K = K *P %1000000007 #존나큰 K와 존나큰 P를 연산할때 ㅈㄴ오래걸리니 연산후 나머지를 해서 수를줄인다
    #A = q*Xa + Ra,B = q*Xb + Rb 두개의 수를 곱하면 몫은 복잡한 식이지만 나머지는 곱해진 두 수 A,B의 나머지 Ra,Rb의 곱 Ra*Rb가 된다.
    #결과적으로 수많은 수;K*P*P*P*P*P~~*P의 경우 각개 두개 곱의 나머지의 곱이 된다.
print(K)