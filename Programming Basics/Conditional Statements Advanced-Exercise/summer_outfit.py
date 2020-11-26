from _ast import If

degrees = int(input())
time_of_day = input()

Outfit = 0
Shoes = 0

if time_of_day == "Morning" and 10 <= degrees <= 18:
    Outfit = "Sweatshirt"
    Shoes = "Sneakers"
    print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")

elif time_of_day == "Afternoon" and 10 <= degrees <= 18:
    Outfit = "Shirt"
    Shoes = "Moccasins"
    print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")

elif time_of_day == "Evening" and 10 <= degrees <= 18:
    Outfit = "Shirt"
    Shoes = "Moccasins"
    print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")

if time_of_day == "Morning" and 18 < degrees <= 24:
    Outfit = "Shirt"
    Shoes = "Moccasins"
    print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")

elif time_of_day == "Afternoon" and 18 < degrees <= 24:
    Outfit = "T-Shirt"
    Shoes = "Sandals"
    print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")

elif time_of_day == "Evening" and 18 < degrees <= 24:
    Outfit = "Shirt"
    Shoes = "Moccasins"
    print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")

if time_of_day == "Morning" and degrees >= 25:
    Outfit = "T-Shirt"
    Shoes = "Sandals"
    print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")

elif time_of_day == "Afternoon" and degrees >= 25:
    Outfit = "Swim Suit"
    Shoes = "Barefoot"
    print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")

elif time_of_day == "Evening" and degrees >= 25:
    Outfit = "Shirt"
    Shoes = "Moccasins"
    print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
