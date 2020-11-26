text = input()
numbers = text.split(", ")
number_of_beggars = int(input())

beggars_list_sum = [0] * number_of_beggars
counter = 0
for num in numbers:
    num = int(num)
    beggars_list_sum[counter] += num
    if counter == number_of_beggars - 1:
        counter = 0
    else:
        counter += 1
print(beggars_list_sum)