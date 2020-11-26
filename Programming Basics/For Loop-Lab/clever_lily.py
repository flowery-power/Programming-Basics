age = int(input())
price = float(input())
toy_price = int(input())
total = 0
for i in range(1, age +1):
    if i % 2 == 0:
        total += 5 * i -1

    else:
        total += toy_price
if total >= price:
    print(f"Yes! {total - price:.2f}")

else:
    total < price
    print(f"No! {price - total:.2f}")
