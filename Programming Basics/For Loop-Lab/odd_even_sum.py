n = int(input())
odd = 0
even = 0
for i in range(1, n+1):
    number1 = int(input())
    if i % 2 == 0:
        even += number1

    else:
        odd += number1

if even == odd:
    print(f"Yes\nSum = {even}")

else:
    print(f"No\nDiff = {abs(odd - even)}")
