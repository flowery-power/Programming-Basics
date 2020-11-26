screening_type = input()
rows = int(input())
columns = int(input())

price = 0
total_price = 0

if screening_type == "Premiere":
    price = 12.00

elif screening_type == "Normal":
    price = 7.50

elif screening_type == "Discount":
    price = 5.00

total_price = price * rows * columns
print(f"{total_price:.2f}")

