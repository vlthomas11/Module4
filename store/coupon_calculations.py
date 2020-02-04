def calculate_price(price, cash_coupon, percent_coupon):
    percent_discount_multiplier = (100 - percent_coupon) / 100
    print(percent_discount_multiplier)

    final_price = (price - cash_coupon) * percent_discount_multiplier
    print(final_price)

    if final_price < 10:
        shipping = 5.95
    elif final_price < 30:
        shipping = 7.95
    elif final_price < 50:
        shipping = 11.95
    elif final_price >= 50:
        shipping = 0
    print(shipping)

    tax = final_price * .06
    final_plus_tax = tax + final_price
    total = final_plus_tax + shipping
    print(tax)
    print(final_plus_tax)
    print(total)


def customer_order():
    price = float(input("What is the price of your item? "))
    cash_coupon = int(input("How much is your cash coupon? "))
    percent_coupon = int(input("How much is your percent coupon? "))
    calculate_price(price, cash_coupon, percent_coupon)


if __name__ == '__main__':
    customer_order()
