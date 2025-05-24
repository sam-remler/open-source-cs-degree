def savings_function():
    yearly_salary = float(input("Enter your starting yearly salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    cost_of_dream_home = float(input("Enter the cost of your dream home: "))
    semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

    portion_down_payment = 0.25
    amount_saved = 0
    annual_return = 0.05

    month = 0

    while cost_of_dream_home * portion_down_payment > amount_saved:
        month += 1
        amount_saved *= (1+ annual_return / 12)
        amount_saved += yearly_salary * portion_saved / 12
        if month % 6 == 0:
            yearly_salary *= (1 + semi_annual_raise)
    
    return month


if __name__ == "__main__":
    month = savings_function()
    print (f"Number of months: {month}")

