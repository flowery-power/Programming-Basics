budjet_film = float(input())
number_staff = int(input())
money_for_one_staff = float(input())

money_for_decore = 0
money_for_decore = budjet_film * 0.1
money_for_close = number_staff * money_for_one_staff
if number_staff > 150:
    money_for_close *= 0.9
money_sum = money_for_decore + money_for_close
if money_sum > budjet_film:
    print("Not enough money!")
    print(f"Wingard needs {abs(money_sum - budjet_film):.2f} leva more.")
if money_sum <= budjet_film:
    print("Action!")
    print(f"Wingard starts filming with {abs(money_sum - budjet_film):.2f} leva left.")