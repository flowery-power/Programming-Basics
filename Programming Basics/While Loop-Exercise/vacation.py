excur_money = float(input())
available_money = float(input())
days_total = 0
days_spend = 0

while True:
    command = input()
    money = float(input())
    days_total += 1

    if command == "spend":
        if money > available_money:
            available_money = 0
        else:
            available_money -= money
        days_spend += 1

    if command == "save":
        available_money += money
        days_spend = 0

    if days_spend >= 5:
        print(f"You can't save the money.\n{days_total}")
        break
    if available_money >= excur_money:
        print(f"You saved the money for {days_total} days.")
        break


