
n = int(input())
scores = list(map(int,input().split()))
m = max(scores)
new_scores = [sc/m*100 for sc in scores]
print(sum(new_scores)/n)
