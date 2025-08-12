# Vacation Budget Calculator
# Plan a 7-day trip for 4 people

# === Fixed Variables ===
trip_days = 7
people = 4
trip_budget = 8000.00
income = 100000.00
flight_cost = 2400.00
hotel_cost = 2400.00
food_cost = 300.00
transportation_cost = 0
# === Get User Input for Expenses (With Error Handling) ===
def get_expense_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

flight_cost = get_expense_input("Enter total flight cost ($): ")
hotel_cost = get_expense_input("Enter total hotel cost ($): ")
food_cost = get_expense_input("Enter total food cost ($): ")

# === Expenses stored as list of dictionaries ===
expenses = [
    {"category": "Flight", "cost": flight_cost},
    {"category": "Hotel", "cost": hotel_cost},
    {"category": "Food", "cost": food_cost}
]

# === Calculate total expenses using loop ===
total_expenses = 0
for item in expenses:
    total_expenses += item["cost"]

# === Display budget comparison ===
print("\n--- Vacation Budget Summary ---")
print("Trip Budget:      ${:.2f}".format(trip_budget))
print("Total Expenses:   ${:.2f}".format(total_expenses))

if total_expenses <= trip_budget:
    print("✅ You're within budget!")
else:
    over = total_expenses - trip_budget
    print("❌ You're over budget by ${:.2f}".format(over))

# === Calculate savings after budget is set aside ===
savings = income - trip_budget
print("Estimated Savings After Budget: ${:.2f}".format(savings))

# === Final Affordability Check ===
if savings >= total_expenses:
    print("🎉 You can afford this trip comfortably!")
else:
    print("⚠️ You need to save more to afford this trip.")

# === Optional: Print breakdown by category ===
print("\n--- Expense Breakdown ---")
for expense in expenses:
    print("- {}: ${:.2f}".format(expense["category"], expense["cost"]))
