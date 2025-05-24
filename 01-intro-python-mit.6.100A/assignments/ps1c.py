def interest_rate_needed():
    initial_deposit = float(input("Enter the initial deposit: "))

    cost_of_dream_home = 800000
    portion_down_payment = 0.25

    month = 36
    steps = 0

    if initial_deposit >= cost_of_dream_home * portion_down_payment:
        return 0, steps
    elif initial_deposit * (1 + 1/12)**month <= cost_of_dream_home * portion_down_payment:
        return None, steps
    else:
        r = 0.5
        r_upper = 1
        r_lower = 0

        while abs(cost_of_dream_home * portion_down_payment - initial_deposit * (1 + r/12)**month) > 100:
            if cost_of_dream_home * portion_down_payment > initial_deposit * (1 + r/12)**month:
                r_lower = r
            else:
                r_upper = r
            
            r = (r_lower + r_upper) / 2
            steps += 1
                
        return r, steps

if __name__ == "__main__":
    r, steps = interest_rate_needed()
    print (f"Best savings rate: {r} \nSteps in bisection search: {steps}")

