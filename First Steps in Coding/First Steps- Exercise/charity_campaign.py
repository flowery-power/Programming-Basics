cake = 45
waffle = 5.80
pancake = 3.20

total_money_for_day = 0
total_money_after_expences = 0

day_campaign = int(input())
number_confectioner = int(input())
number_cake = int(input())
number_waffle = int(input())
number_pancake = int(input())

cake_sum = number_cake * cake
waffle_sum = number_waffle * waffle
pancake_sum = number_pancake * pancake

total_money_for_day = (cake_sum + waffle_sum + pancake_sum) * number_confectioner
total_sum_for_campain = total_money_for_day * day_campaign
total_money_after_expences = total_sum_for_campain -1/8 * total_sum_for_campain
print(total_money_after_expences)
