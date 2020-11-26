import sys
max = -sys.maxsize

command = input()
while command != "Stop":
    num =int(command)

    if num > max:
        max = num
    command = input()
print(max)