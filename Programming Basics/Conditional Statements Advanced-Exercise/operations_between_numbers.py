num1 = int(input())
num2 = int(input())
operator = input()


if operator == "+":
    total = num1 + num2
    if total % 2 == 0:
        print(f"{num1} {operator} {num2} = {total} - even")
    else:
        print(f"{num1} {operator} {num2} = {total} - odd")


elif operator == "-":
    total = num1 - num2
    if total % 2 == 0:
        print(f"{num1} {operator} {num2} = {total} - even")

    else:
        print(f"{num1} {operator} {num2} = {total} - odd")


elif operator == "*":
    total = num1 * num2
    if total % 2 == 0:
        print(f"{num1} {operator} {num2} = {total} - even")

    else:
        print(f"{num1} {operator} {num2} = {total} - odd")

elif operator == "/":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")


    else:
        total = num1 / num2
        print(f"{num1} / {num2} = {total:.2f}")

elif operator == "%":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")

    else:
        total = num1 % num2
        print(f"{num1} % {num2} = {total}")


