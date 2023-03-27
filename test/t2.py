def solution(n, results):
    answer = 0

    graph = {i:[set(),set()] for i in range(1,n+1)}

    for w,l in results:
        graph[w][0].add(l)
        graph[l][1].add(w)
    
    for p in range(1,n+1):
        for l in graph[p][0]:
            graph[l][1] |= graph[p][1]
        
        for w in graph[p][1]:
            graph[w][0] |= graph[p][0]
    
    for p,(win,lose) in graph.items():
        if len(win) + len(lose) == n-1: answer += 1

    for i in graph:
        print(graph[i])

    return answer