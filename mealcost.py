def solve(meal_cost, tip_percent, tax_percent):
    tip_value = tip_percent * (meal_cost/100)
    tax_value = tax_percent * (meal_cost/100)
    total_cost = meal_cost + tip_value + tax_value
    total_cost = round(total_cost)
    print(f"{total_cost}")

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)