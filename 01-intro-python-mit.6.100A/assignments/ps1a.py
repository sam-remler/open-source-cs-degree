def savings_function():
    try:
        yearly_salary = float(input("Enter your starting yearly salary: "))
        portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
        cost_of_dream_home = float(input("Enter the cost of your dream home: "))
    except:
        ValueError("Those are not valid inputs")

    portion_down_payment = 0.25
    amount_saved = 0
    annual_return = 0.05

    month = 0

    while cost_of_dream_home * portion_down_payment > amount_saved:
        amount_saved *= (1+ annual_return / 12)
        amount_saved += yearly_salary * portion_saved / 12
        month += 1
    
    return month


if __name__ == "__main__":
    month = savings_function()
    print (f"Number of months: {month}")

