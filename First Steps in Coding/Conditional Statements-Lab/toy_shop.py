puzzle_price = 2.60
talking_doll = 3
teddy_bear = 4.10
minion = 8.20
truck = 2

price_ekcursion = float(input())
number_puzzle = int(input())
number_talking_dols = int(input())
number_teddy_bear = int(input())
number_minion = int(input())
number_truck = int(input())

sum = (number_puzzle * puzzle_price) + (number_talking_dols * talking_doll) + (number_teddy_bear * teddy_bear) + (number_minion * minion) + (number_truck * truck)
number_toys = number_puzzle + number_talking_dols + number_truck + number_minion + number_teddy_bear
discount = 0

if number_toys >= 50:
    discount = 0.25 * sum

final_price = sum - discount
rent = 0.10 * final_price
profit = final_price - rent

if profit >= price_ekcursion:
    print(f'Yes!{ profit - price_ekcursion: .2f} lv left.')
else:
    print(f'Not enough money!{price_ekcursion - profit: .2f} lv needed.')




