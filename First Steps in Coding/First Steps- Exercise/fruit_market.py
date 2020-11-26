strawberry_price = float(input())
quantity_banana = float(input())
quantity_oranges = float(input())
quantity_raspberries = float(input())
quantity_strawberry = float(input())


price_raspberries = strawberry_price / 2
price_oranges = price_raspberries * 0.6
price_banana = price_raspberries * 0.2


needed_money = strawberry_price * quantity_strawberry + price_banana * quantity_banana + price_oranges * quantity_oranges + price_raspberries * quantity_raspberries
print(needed_money)