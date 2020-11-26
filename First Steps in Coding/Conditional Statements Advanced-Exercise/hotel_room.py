month = input()
num_night = int(input())

price_night_studio = 0
price_night_apartament = 0

if month == "May" or month == "October":
    price_night_apartament = num_night * 65
    price_night_studio = num_night * 50
    if num_night > 14:
        price_night_studio *= 0.70

    elif num_night > 7:
        price_night_studio *= 0.95

elif month == "June" or month == "September":
    price_night_apartament = num_night * 68.70
    price_night_studio = num_night * 75.20

    if num_night > 14:
        price_night_studio *= 0.80


elif month == "July" or month == "August":
    price_night_apartament = num_night * 77
    price_night_studio = num_night * 76

if num_night > 14:
    price_night_apartament *= 0.9

print(f"Apartment: {price_night_apartament:.2f} lv.")
print(f"Studio: {price_night_studio:.2f} lv.")






