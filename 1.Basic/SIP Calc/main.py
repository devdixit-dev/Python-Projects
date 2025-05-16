import time

def sip_calc():
    print('\n🧮 SIP CALCULATOR')
    print('----------------------------------------------------------')

    # Input: Monthly investment amount
    user_monthly_inv_amount = int(input('Enter your monthly investment amount (e.g., 5000): '))
    time.sleep(1)

    # Input: Annual expected return in %
    user_percent_annum = float(input('Enter expected annual return (e.g., 12): '))
    time.sleep(1)

    # Input: Investment duration in years
    user_inv_duration_year = int(input('Enter investment duration in years (e.g., 5): '))
    time.sleep(1)

    print('----------------------------------------------------------')

    # Core values
    P = user_monthly_inv_amount                   # Monthly investment
    r = (user_percent_annum / 100) / 12           # Monthly interest rate
    n = user_inv_duration_year * 12               # Total number of months

    # Future value formula for annuity due (SIP)
    fv = P * (((1 + r) ** n - 1) / r) * (1 + r)

    # Total amount invested
    total_invested = P * n
    estimated_gain = fv - total_invested

    time.sleep(1)

    print('\n📊 SIP SUMMARY')
    print('----------------------------------------------------------')
    print(f"📅 Duration            : {user_inv_duration_year} years ({n} months)")
    print(f"💸 Monthly Investment  : ₹{P:,}")
    print(f"📈 Expected Return     : {user_percent_annum}% per annum")
    print('----------------------------------------------------------')
    print(f"💰 Total Invested      : ₹{total_invested:,.2f}")
    print(f"📦 Future Value        : ₹{fv:,.2f}")
    print(f"📊 Estimated Gain      : ₹{estimated_gain:,.2f}")
    print('----------------------------------------------------------\n')

# Run the calculator
sip_calc()