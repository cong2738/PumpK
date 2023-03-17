#i+1번째로 끝난 경우의 징검다리 수는 i까지의 해당 숫자로 끝난 경우의 수중 가장 큰 경우의 +1이다
#ends[i] = max([ends[j] for j in range(i) if Rock_i > Rock_j])
N = int(input())
bridge = list(map(int,input().split()))
end = [1]*N #i번째로 끝난 경우의 징검다리 수.dpmemo
for i in range(N): 
    end[i] = max([0] + [end[j] for j in range(i) if bridge[i] > bridge[j]]) + 1
print(end)
print(max(end))