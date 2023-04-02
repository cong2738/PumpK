from collections import defaultdict as dd

data = dd(list)
while True:
    try: line = input()
    except EOFError: break
    data[''.join(sorted(line.rstrip()))].append(line.rstrip())

anagram = [sorted(val) for val in data.values()]
anagram.sort(key=lambda x:(-len(x),x))

for group in anagram[:5]:
   print(f'Group of size {len(group)}: {" ".join([elem for elem in sorted(list(set(group)))])} .')