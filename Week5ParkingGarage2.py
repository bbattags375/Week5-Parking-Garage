
BASE_FEE = 5.00
HOURLY_RATE = 2.50
PERCENT_DISCOUNT = 0.20
DOLLAR_DISCOUNT = 2.00
FLAT_RATE = 20.00

hours = float(input("Enter hours parked: "))

fee = BASE_FEE + (HOURLY_RATE * hours)

coupon = input("Enter discount coupon type ($=dollar off, %=percent off, f=flat rate): ").strip().lower()

if coupon == "%":
    fee = fee * (1 - PERCENT_DISCOUNT)
elif coupon == "$":
    fee = fee - DOLLAR_DISCOUNT
elif coupon == "f":
    fee = FLAT_RATE

print(f"Parking fee: $ {fee:.2f}")