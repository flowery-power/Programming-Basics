text = input()
numbers = text.split(" ")
num = int(input())
my_list_sortet = []
list_result = []

for number in numbers:
    my_list_sortet.append(int(number))
my_list_sortet.sort()
my_list_sortet = my_list_sortet[:num]

for number in numbers:
    number = int(number)
    if not my_list_sortet.__contains__(number):
        list_result.append(int(number))
print(list_result)

