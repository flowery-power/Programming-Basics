import sys

n = int(input())
max_num = -sys.maxsize
total_sum = 0

for i in range(1, n + 1):
    number = int(input())
    total_sum += number
    if number > max_num:
        max_num = number

other_sum = total_sum - max_num
if max_num == other_sum:
    print("Yes")
    print(f"Sum = {other_sum}")
else:
    print("No")
    print(f"Diff = {abs(max_num - other_sum)}")

