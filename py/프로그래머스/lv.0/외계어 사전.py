def solution(spell, dic):
    for word in dic:
        for c in spell:
            if word.count(c) != 1: break
        else: return 2
    return 1