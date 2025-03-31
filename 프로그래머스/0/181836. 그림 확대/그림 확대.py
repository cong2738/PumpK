def solution(picture, k):
    answer = []
    for row in picture:
        new_row = ''
        for pix in row:
            new_row += pix*k
        for _ in range(k):
            answer.append(new_row)
    return answer