money = input()
money_sum = 0

while money != "NoMoreMoney":
    money = float(money)
    if money < 0:
        print("Invalid operation!")
        isInvalidOperation = True
        break
    money_sum += money
    print(f"Increase: {money:.2f}")
    money = input()

print(f"Total: {money_sum:.2f}")
