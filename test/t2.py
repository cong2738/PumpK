def solution(scores):
    answer = 1

    target = scores[0]
    target_score = sum(scores[0])
    print(sorted(scores,key=lambda x:-sum(x)))
    scores.sort(key=lambda x: (-x[0],x[1]))
    print(scores)

    threshold = 0
    for score in scores:
        if target[0] < score[0] and target[1] < score[1]:
            return -1
        if threshold <= score[1]:
            if target_score < score[0] + score[1]:
                answer += 1
            threshold = score[1]
    return answer

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))