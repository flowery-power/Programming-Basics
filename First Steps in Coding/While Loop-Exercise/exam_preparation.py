not_good_grades = int(input())

counter_done_task = 0
counter_low_grades = 0
total_grades = 0
last_task = 0
has_failed = False

while True:
    name_task = input()
    if name_task == "Enough":
        break

    grade = int(input())

    if grade <= 4:
        counter_low_grades += 1
    else:
        counter_done_task += 1

    if counter_low_grades == not_good_grades:
        has_failed = True
        break

    total_grades += grade
    last_task = name_task

count_all_grades = counter_low_grades + counter_done_task
average = total_grades / count_all_grades
if has_failed:
    print(f"You need a break, {counter_low_grades} poor grades.")
else:
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {count_all_grades}")
    print(f"Last problem: {last_task}")