def solution(participant, completion):
    cpmap = dict()
    for cp in completion:
        if cp in cpmap:
            cpmap[cp] += 1
        else:
            cpmap[cp] = 1
    for pa in participant:
        if pa in cpmap:
            cpmap[pa] -= 1
            if cpmap[pa] == 0:
                cpmap.pop(pa)
        else:
            return pa
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]	
completion = ["josipa", "filipa", "marina", "nikola"]	
print(solution(participant, completion))
