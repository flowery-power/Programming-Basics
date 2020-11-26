text = input()

cards = text.split(" ")
faro_shuffle_numbers = int(input())


def faro_shuffle(cards):
    deck_len = len(cards)
    faro_shuffle_list = []
    small_deck_len = int(deck_len / 2)
    small_deck1 = cards[0:small_deck_len]
    small_deck2 = cards[small_deck_len:deck_len]

    for i in range(small_deck_len):
        faro_shuffle_list.append(small_deck1[i])
        faro_shuffle_list.append(small_deck2[i])
    return faro_shuffle_list


for i in range(faro_shuffle_numbers):
    cards = faro_shuffle(cards)
print(cards)
