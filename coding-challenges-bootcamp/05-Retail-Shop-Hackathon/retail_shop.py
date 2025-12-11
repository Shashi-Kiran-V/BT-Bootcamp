# Integrated Retail Billing System with Promotions, Discounts, Tax, Payment, Minimum Purchase, and Loyalty Points

PROMO_CODES = {
    "PROMO10": 0.10  # 10% discount
}

def get_item_details():
    """Accepts item details from the user with validation."""
    try:
        item_code = input("Enter Item Code: ").strip()
        description = input("Enter Item Description: ").strip()
        
        quantity = float(input("Enter Quantity: "))
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        price = float(input("Enter Price per Unit: ₹"))
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        return item_code, description, quantity, price
    except ValueError as e:
        print("Error:", e)
        return get_item_details()
    except Exception:
        print("Something went wrong! Please check your inputs.")
        return get_item_details()

def calculate_total(quantity, price):
    return quantity * price

def apply_promotional_discount(item_code, total):
    """Applies promotional discount if item code matches."""
    if item_code in PROMO_CODES:
        discount_rate = PROMO_CODES[item_code]
        discount_amount = total * discount_rate
        total_after_discount = total - discount_amount
        return total_after_discount, discount_amount
    return total, 0

def display_item_total(item_code, description, quantity, price, total, promo_discount=0):
    print("\n----- Item Total -----")
    print(f"Item Code       : {item_code}")
    print(f"Description     : {description}")
    print(f"Quantity        : {quantity}")
    print(f"Price per Unit  : ₹{price}")
    if promo_discount > 0:
        print(f"Promotional Discount Applied: -₹{promo_discount:,.2f}")
    print(f"Total Cost      : ₹{total:,.2f}")

def apply_discounts(grand_total, total_quantity):
    discount_details = []
    modified_total = grand_total

    if grand_total > 10000:
        discount1 = 0.10 * modified_total
        modified_total -= discount1
        discount_details.append(f"10% discount for grand total > ₹10,000: -₹{discount1:,.2f}")
    if total_quantity > 20:
        discount2 = 0.05 * modified_total
        modified_total -= discount2
        discount_details.append(f"5% additional discount for quantity > 20: -₹{discount2:,.2f}")

    return modified_total, discount_details

def apply_membership_discount(grand_total, is_member):
    if is_member:
        discount = 0.02 * grand_total
        grand_total -= discount
        return grand_total, f"2% membership discount applied: -₹{discount:,.2f}"
    return grand_total, None

def calculate_tax(grand_total):
    """Apply tiered tax rates based on grand total."""
    if grand_total < 5000:
        tax_rate = 0.05
    elif 5000 <= grand_total <= 20000:
        tax_rate = 0.10
    else:
        tax_rate = 0.15
    tax_amount = grand_total * tax_rate
    grand_total_with_tax = grand_total + tax_amount
    return tax_amount, grand_total_with_tax, tax_rate*100

def apply_payment_surcharge(grand_total_with_tax, payment_mode):
    """Applies 2% surcharge if payment mode is Credit Card."""
    surcharge = 0
    if payment_mode.lower() == "credit card":
        surcharge = 0.02 * grand_total_with_tax
        grand_total_with_tax += surcharge
    return grand_total_with_tax, surcharge

def calculate_loyalty_points(final_amount):
    """Calculate loyalty points earned based on ₹100 per point."""
    return int(final_amount // 100)

# -------- MAIN PROGRAM --------
grand_total = 0
total_quantity = 0
items = []

# Item Entry Loop
while True:
    item_code, description, quantity, price = get_item_details()
    
    total = calculate_total(quantity, price)
    total_after_discount, promo_discount = apply_promotional_discount(item_code, total)
    
    grand_total += total_after_discount
    total_quantity += quantity
    items.append((item_code, description, quantity, price, total_after_discount, promo_discount))
    
    display_item_total(item_code, description, quantity, price, total_after_discount, promo_discount)
    
    more = input("\nDo you want to enter another item? (y/n): ").strip().lower()
    if more != 'y':
        break

# Apply standard discounts
final_total, discount_details = apply_discounts(grand_total, total_quantity)

# Membership discount
membership = input("\nAre you a member? (y/n): ").strip().lower()
final_total, membership_detail = apply_membership_discount(final_total, membership == 'y')

# Tax calculation
tax_amount, final_total_with_tax, tax_rate = calculate_tax(final_total)

# Payment mode
payment_mode = input("\nSelect Payment Mode (Cash/Credit Card): ").strip()
final_payable, surcharge = apply_payment_surcharge(final_total_with_tax, payment_mode)

# Minimum Purchase Check
MIN_PURCHASE = 500
if final_payable < MIN_PURCHASE:
    print("\n===================================")
    print(f"Invoice cannot be generated. Minimum purchase amount of ₹{MIN_PURCHASE} not met.")
    print(f"Your final total is ₹{final_payable:,.2f}")
    print("===================================")
else:
    # Calculate loyalty points
    loyalty_points = calculate_loyalty_points(final_payable)

    # Display Final Bill
    print("\n===============================")
    print(f"Grand Total before discounts: ₹{grand_total:,.2f}")
    if discount_details:
        print("Discounts Applied:")
        for detail in discount_details:
            print(detail)
    if membership_detail:
        print(membership_detail)
    print(f"Subtotal after discounts: ₹{final_total:,.2f}")
    print(f"Applied Tax ({tax_rate}%): ₹{tax_amount:,.2f}")
    if surcharge > 0:
        print(f"{payment_mode} Surcharge (2%): ₹{surcharge:,.2f}")
    print(f"Final Payable Amount: ₹{final_payable:,.2f}")
    print(f"Payment Mode: {payment_mode}")
    print(f"Loyalty Points Earned: {loyalty_points}")
    print("===============================")
