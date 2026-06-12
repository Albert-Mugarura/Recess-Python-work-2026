print("E-COMMERCE SYSTEM")
print("=" * 40)

# LOGIN SYSTEM
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "admin123":
    role = "Admin"
elif username == "customer" and password == "cust123":
    role = "Customer"
elif username == "cashier" and password == "cash123":
    role = "Cashier"
else:
    print("Invalid username or password!")
    exit()

print(f"\nLogin Successful! Welcome {role}")

# ACCESS LEVELS
if role == "Admin":
    print("Access: All Features")
elif role == "Cashier":
    print("Access: Sales and Billing")
else:
    print("Access: Shopping Features")

print("\nPRODUCT PURCHASE")
print("-" * 30)

# Product Details
subtotal = float(input("Enter subtotal amount: "))

# Discount based on subtotal
if subtotal >= 500000:
    discount = 0.20
elif subtotal >= 200000:
    discount = 0.10
elif subtotal >= 100000:
    discount = 0.05
else:
    discount = 0

discount_amount = subtotal * discount

# Coupon Code Validation
coupon = input("Enter coupon code: ")

if coupon == "SAVE10":
    coupon_discount = subtotal * 0.10
    print("Valid Coupon! Extra 10% discount applied.")
elif coupon == "SAVE5":
    coupon_discount = subtotal * 0.05
    print("Valid Coupon! Extra 5% discount applied.")
else:
    coupon_discount = 0
    print("Invalid Coupon Code!")

# Price after discounts
price_after_discount = subtotal - discount_amount - coupon_discount

# Location-based Tax
location = input("Enter location (Kampala/Entebbe/Jinja): ")

if location.lower() == "kampala":
    tax_rate = 0.18
elif location.lower() == "entebbe":
    tax_rate = 0.15
elif location.lower() == "jinja":
    tax_rate = 0.12
else:
    tax_rate = 0.10

tax_amount = price_after_discount * tax_rate

# Final Price
final_price = price_after_discount + tax_amount

# Receipt
print("\n" + "=" * 40)
print("PURCHASE SUMMARY")
print("=" * 40)
print(f"Subtotal: UGX {subtotal:,.0f}")
print(f"Discount: UGX {discount_amount:,.0f}")
print(f"Coupon Discount: UGX {coupon_discount:,.0f}")
print(f"Tax: UGX {tax_amount:,.0f}")
print(f"Final Price: UGX {final_price:,.0f}")
print("=" * 40)