import math

figure = input()
if figure == "square":
    side = float(input())
    print(f'{side * side: 3f}')


if figure == "rectangle":
    sideA = float(input())
    sideB = float(input())
    print(f'{sideA * sideB: .3f}')

if figure == "circle":
    radius = float(input())
    print(f'{math.pi * radius *radius : 3f}')

if figure == "triangle":
    side = float(input())
    height = float(input())
    print(f'{(side * height) /2: .3f}')






