budget = float(input())
season = input()
num_fisherman = float(input())

total_money = 0
discount = 0
rent_ship = 0

if season == "Spring":
    rent_ship = 3000

elif season == "Summer":
    rent_ship = 4200

elif season == "Autumn":
    rent_ship = 4200

elif season == "Winter":
    rent_ship = 2600

if num_fisherman <= 6:
    discount = 0.9

if 7 <= num_fisherman <= 11:
    discount = 0.85
if num_fisherman >= 12:
    discount = 0.75

total_money = rent_ship * discount

if num_fisherman % 2 == 0 and season != "Autumn":
    total_money *= 0.95

if budget < total_money:
    print(f"Not enough money! You need {total_money - budget:.2f} leva.")
else:
    print(f"Yes! You have {budget - total_money:.2f} leva left.")
