n = int(input())
word = input()

my_list = []
word_list = []
for index in range(n):
    text = input()
    if word in text:
        word_list.append(text)
    my_list.append(text)
print(my_list)
print(word_list)

