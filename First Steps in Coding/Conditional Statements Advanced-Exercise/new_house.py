kind_flowers = input()
number_flowers = int(input())
budget = int(input())

discount = 1

if kind_flowers == "Roses":
    price = 5
    if number_flowers > 80:
        discount *= 0.9

elif kind_flowers == "Dahlias":
    price = 3.80
    if number_flowers > 90:
        discount *= 0.85

elif kind_flowers == "Tulips":
    price = 2.80
    if number_flowers > 80:
        discount *= 0.85

elif kind_flowers == "Narcissus":
    price = 3
    if number_flowers < 120:
        discount *= 1.15

elif kind_flowers == "Gladiolus":
    price = 2.50
    if number_flowers < 80:
        discount *= 1.20

total_bulshit = number_flowers * price
total_bulshit *= discount

if total_bulshit > budget:
    print(f"Not enough money, you need {(total_bulshit - budget):.2f} leva more.")

elif total_bulshit <= budget:
    print(f"Hey, you have a great garden with {number_flowers} {kind_flowers} and {abs(budget-total_bulshit):.2f} leva left.")
