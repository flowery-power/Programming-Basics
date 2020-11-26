import math


record_in_secound = float(input())
distance_in_meters = float(input())
time_secound_distance = float(input())

total_time = 0
must_swim = 0
added_seconds = 0

must_swim = distance_in_meters * time_secound_distance
added_seconds = math.floor(distance_in_meters / 15) * 12.5
total_time = must_swim + added_seconds

if record_in_secound <= total_time:
    print(f"No, he failed! He was {total_time - record_in_secound:.2f} seconds slower.")
if record_in_secound > total_time:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
