budget = float(input())
season = input()

holiday = ""
destination = ""
price_night = 0

if season == "summer":
    holiday = "Camp"
if season == "winter":
    holiday = "Hotel"

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price_night = budget * 0.3
    elif season == "winter":
        price_night = budget * 0.7

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price_night = budget * 0.4
    elif season == "winter":
        price_night = budget * 0.8

elif budget >= 1000:
    destination = "Europe"
    price_night = budget * 0.9
    holiday = "Hotel"



print(f"Somewhere in {destination}")
print(f"{holiday} - {price_night:.2f}")