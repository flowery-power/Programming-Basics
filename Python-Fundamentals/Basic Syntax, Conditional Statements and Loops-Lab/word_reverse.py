text = input()
revers_word = ""

for i in range(len(text) -1, -1,-1):
    revers_word += text[i]
print(revers_word)
