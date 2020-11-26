import sys
min = sys.maxsize

command = input()
while command != "Stop":
    num =int(command)

    if num < min:
        min = num
    command = input()
print(min)