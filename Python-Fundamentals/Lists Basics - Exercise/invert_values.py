text = input()

numbers = text.split(" ")
opposite_num_list = []

for number in numbers:
    number = int(number)
    number = -number
    opposite_num_list.append(number)

print(opposite_num_list)

