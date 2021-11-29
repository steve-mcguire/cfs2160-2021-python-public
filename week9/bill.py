# cost after tax will be the initial cost plus 6.75% of the initial cost
import locale
locale.setlocale(locale.LC_ALL, 'en_GB')


def calculate_bill(meal_cost, pay_tip=False):
    tax = 6.75
    tip = 15
    # meal_cost = 44.50
    meal_tax = meal_cost * (tax / 100)
    meal_tip = 0
    if pay_tip:
        meal_tip = (meal_cost + meal_tax) * (tip / 100)
    return meal_cost + meal_tax + meal_tip


print(locale.currency(calculate_bill(44.50, False)))

