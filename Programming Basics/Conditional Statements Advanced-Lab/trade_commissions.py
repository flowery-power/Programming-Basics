city = input()
volume_sales = float(input())

if city == "Sofia":
    if 0 <= volume_sales <= 500:
        print(f"{volume_sales * 0.05:.2f}")
    elif 500 < volume_sales <= 1000:
        print(f"{ volume_sales * 0.07:.2f}")
    elif 1000 < volume_sales <= 10000:
        print(f"{volume_sales * 0.08:.2f}")
    elif volume_sales > 10000:
        print(f"{volume_sales * 0.12:.2f}")

    else:
        print("error")

elif city == "Varna":
    if 0 <= volume_sales <= 500:
        print(f"{volume_sales * 0.045:.2f}")
    elif 500 < volume_sales <= 1000:
        print(f"{ volume_sales * 0.075:.2f}")
    elif 1000 < volume_sales <= 10000:
        print(f"{volume_sales * 0.1:.2f}")
    elif volume_sales > 10000:
        print(f"{volume_sales * 0.13:.2f}")

    else:
        print("error")

elif city == "Plovdiv":
    if 0 <= volume_sales <= 500:
        print(f"{volume_sales * 0.055:.2f}")
    elif 500 < volume_sales <= 1000:
        print(f"{volume_sales * 0.08:.2f}")
    elif 1000 < volume_sales <= 10000:
        print(f"{volume_sales * 0.12:.2f}")
    elif volume_sales > 10000:
        print(f"{volume_sales * 0.145:.2f}")
    else:
        print("error")
else:
    print("error")






