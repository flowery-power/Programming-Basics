number = int(input())
number_printing = 1
for row in range(1, number + 1):
    for colum in range(1, row + 1):
        print(f"{number_printing}", end=' ')
        number_printing += 1
        if number_printing > number:
            break

    if number_printing > number:
        break
    print()
