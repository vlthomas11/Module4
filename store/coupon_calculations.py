"""
Program: coupon_calculations.py
Author: Vickilee Thomas
Last Modified Date 2/4/2020

The purpose of this program is to calculate the total cost a customer owes after discounts, taxes, and shipping costs.
"""



def calculate_price(price, cash_coupon, percent_coupon):
    percent_discount_multiplier = (100 - percent_coupon) / 100

    final_price = (price - cash_coupon) * percent_discount_multiplier

    if final_price < 10:
        shipping = 5.95
    elif final_price < 30:
        shipping = 7.95
    elif final_price < 50:
        shipping = 11.95
    elif final_price >= 50:
        shipping = 0

    tax = final_price * .06
    total = final_price + tax + shipping

    return total


def customer_order():
    price = float(input("What is the price of your item? "))
    cash_coupon = int(input("How much is your cash coupon? "))
    percent_coupon = int(input("How much is your percent coupon? "))
    total_cost = calculate_price(price, cash_coupon, percent_coupon)
    rounded_total = round(total_cost, 2)
    print("The you total cost is $",rounded_total)


if __name__ == '__main__':
    customer_order()
