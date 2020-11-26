n = int(input())

num1 = 0
num2 = 0
sum = 0

for i in range(1, n + 1):
    new = int(input())
    num1 += new

for j in range(1, n + 1):
    new = int(input())
    num2 += new

if num1 == num2:
    print(f'Yes, sum = {num1 }')
else:
    print(f"No, diff = {abs(num1 - num2)}")