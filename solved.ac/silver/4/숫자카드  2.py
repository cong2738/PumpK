from collections import Counter
input()
SangGeun = input().split()
input()
cards = input().split()
SangGeun_cards = Counter(SangGeun)
print(' '.join(str(SangGeun_cards[card]) if card in SangGeun_cards else '0' for card in cards))