# ================= HEALWELL CARE HOSPITAL BILLING SYSTEM =================

# ------------------ LEVEL 7: ADMIN SETUP OF SERVICES ------------------

def setup_services():
    print("===== ADMIN: Set Up Services of the Day =====")
    services = []
    costs = []

    while True:
        try:
            n = int(input("Enter number of services to configure: "))
            if n <= 0:
                print("❌ Number of services must be positive.")
                continue
            break
        except ValueError:
            print("❌ Enter a valid number.")

    for i in range(n):
        while True:
            name = input(f"Enter name of service {i+1}: ").strip()
            if not name:
                print("❌ Service name cannot be empty.")
                continue
            if name in services:
                print("❌ Service already exists, enter a different name.")
                continue
            break
        while True:
            try:
                cost = float(input(f"Enter cost for '{name}': ₹"))
                if cost < 0:
                    print("❌ Cost cannot be negative.")
                    continue
                break
            except ValueError:
                print("❌ Enter a valid number for cost.")
        services.append(name)
        costs.append(cost)

    print("\n✔ Services configured successfully!\n")
    return services, costs


# ------------------ VALIDATIONS ------------------

def validate_name(name):
    return name.replace(" ", "").isalpha() and len(name) <= 50

def validate_age(age):
    return age.isdigit() and 0 < int(age) <= 120

def validate_gender(gender):
    return gender.lower() in ["male", "female", "other"]

def validate_contact(contact):
    return contact.isdigit() and len(contact) == 10


# ------------------ LEVEL 1: PATIENT DETAILS ------------------

def get_patient_details():
    while True:
        name = input("Enter Patient Name: ").strip()
        if not validate_name(name):
            print("❌ Invalid name! Enter alphabets only.")
            continue

        age = input("Enter Age: ").strip()
        if not validate_age(age):
            print("❌ Invalid age! Enter between 1 to 120.")
            continue

        gender = input("Enter Gender (Male/Female/Other): ").strip()
        if not validate_gender(gender):
            print("❌ Invalid gender!")
            continue

        contact = input("Enter Contact Number (10 digits): ").strip()
        if not validate_contact(contact):
            print("❌ Invalid contact number!")
            continue

        print("\n✔ Patient details recorded.\n")
        return name, int(age), gender.capitalize(), contact


# ------------------ LEVEL 2: DISPLAY & SELECT SERVICES ------------------

def display_services(services, costs):
    print("\n===== AVAILABLE SERVICES =====")
    for i in range(len(services)):
        print(f"{i+1}. {services[i]} - ₹{costs[i]}")


def get_service_selection(services):
    selected_services = []

    print("\nSelect services (0 to finish):")
    while True:
        try:
            choice = int(input("Enter service number: "))
            if choice == 0:
                break
            if 1 <= choice <= len(services):
                service_name = services[choice - 1]
                if service_name in selected_services:
                    print("❌ Service already selected! Choose another.")
                else:
                    selected_services.append(service_name)
                    print(f"✔ Added: {service_name}")
            else:
                print("❌ Invalid option!")
        except ValueError:
            print("❌ Numbers only!")

    return selected_services


# ------------------ LEVEL 3: FETCH COSTS ------------------

def fetch_selected_costs(selected_services, services, costs):
    selected_costs = []
    for s in selected_services:
        if s in services:
            index = services.index(s)
            selected_costs.append(costs[index])
    return selected_costs


# ------------------ LEVEL 4: TOTAL COST ------------------

def calculate_total_cost(cost_list):
    return sum(cost_list)


# ------------------ LEVEL 8: APPLY DISCOUNTS ------------------

def apply_discounts(subtotal, age):
    discount_details = []
    modified_total = subtotal

    # Senior Citizen Discount
    if age >= 60:
        senior_discount = 0.10 * modified_total
        modified_total -= senior_discount
        discount_details.append(f"Senior Citizen Discount (10%): -₹{senior_discount:.2f}")

    # High-Bill Discount
    if modified_total > 5000:
        high_bill_discount = 0.05 * modified_total
        modified_total -= high_bill_discount
        discount_details.append(f"High-Bill Discount (5%): -₹{high_bill_discount:.2f}")

    return modified_total, discount_details


# ------------------ LEVEL 5: GST CALCULATION ------------------

def calculate_gst(total, gst_rate=0.18):
    gst_amount = total * gst_rate
    grand_total = total + gst_amount
    return gst_amount, grand_total


# ------------------ LEVEL 6: GENERATE INVOICE ------------------

def generate_invoice(name, age, gender, contact, selected_services, selected_costs, subtotal, discount_details, gst_amount, grand_total):
    print("\n" + "-"*55)
    print("             HealWell Care Hospital")
    print("                  Patient Invoice")
    print("-"*55)
    print("Patient Information:")
    print(f"Name   : {name}")
    print(f"Age    : {age}")
    print(f"Gender : {gender}")
    print(f"Contact: {contact}\n")

    print("Services Availed:")
    for i, s in enumerate(selected_services):
        print(f"{i+1}. {s} : ₹{selected_costs[i]}")

    print(f"\nSubtotal: ₹{subtotal:.2f}")
    if discount_details:
        print("Discounts Applied:")
        for d in discount_details:
            print(d)
    print(f"GST (18%): ₹{gst_amount:.2f}")
    print(f"Grand Total: ₹{grand_total:.2f}")
    print("\nThank you for choosing HealWell Care Hospital!")
    print("-"*55)


# ------------------ MAIN PROGRAM ------------------

print("===== HEALWELL CARE HOSPITAL SYSTEM =====")

# Step 0 → Admin sets up services
services, costs = setup_services()

# Step 1 → Patient details
name, age, gender, contact = get_patient_details()

# Step 2 → Show services & take selection
display_services(services, costs)
selected_services = get_service_selection(services)

# Step 3 → Fetch costs
selected_costs = fetch_selected_costs(selected_services, services, costs)

# Step 4 → Total cost
total_cost = calculate_total_cost(selected_costs)

# Step 4.5 → Apply Discounts
subtotal_after_discounts, discount_details = apply_discounts(total_cost, age)

# Step 5 → Apply GST
gst_amount, grand_total = calculate_gst(subtotal_after_discounts)

# Step 6 → Generate Invoice
generate_invoice(name, age, gender, contact, selected_services, selected_costs, total_cost, discount_details, gst_amount, grand_total)
