lenght_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
percent_volume = float(input())

volume_fish_tank = 0
total_volume_lt = 0
volume_fish_tank = lenght_in_cm * width_in_cm * height_in_cm
total_volume_lt = volume_fish_tank * 0.001
percent_volume *= 0.01
needed_lt = total_volume_lt *(1-percent_volume)
print(needed_lt)