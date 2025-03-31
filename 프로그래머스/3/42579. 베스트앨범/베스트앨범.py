from collections import defaultdict as dd

def solution(genres, plays):
    dicdic = dd(list)
    genre_palys = dd(int)
    for i in range(len(genres)):
        dicdic[genres[i]]. append((i,plays[i]))
        genre_palys[genres[i]] += plays[i]
    for key in dicdic.keys():
        dicdic[key].sort(key = lambda a : -a[1])        
        
    answer = []
    for key,playsum in sorted(genre_palys.items(),reverse = True, key = lambda a:a[1]):
        answer.append(dicdic[key][0][0])
        if(len(dicdic[key]) > 1):
            answer.append(dicdic[key][1][0])
    return answer