import sys
max_number = -sys.maxsize - 1
min_number = sys.maxsize

n = int(input())

for i in range(n):
    new = int(input())
    if new > max_number:
       max_number = new

    if new < min_number:
     min_number = new

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")