# === Vacation Budget Calculator ===
# This program helps users plan a vacation by comparing trip costs to their set budget.

# === Functions ===

def get_positive_float(prompt, max_limit=10000.0):
    """
    Prompt user for a float input and ensure it doesn't exceed the max_limit.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("❌ Please enter a positive value.")
            elif value > max_limit:
                print(f"⚠️ Value too high. Please enter a value less than ${max_limit}.")
            else:
                return value
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def calculate_total_cost(costs):
    """
    Returns the total of all costs provided in the list.
    """
    return sum(costs)

def compare_budget(total_cost, budget):
    """
    Compare the total trip cost to the user's budget and print the result.
    """
    if total_cost > budget:
        print(f"\n⚠️ You are OVER budget by ${total_cost - budget:.2f}")
    elif total_cost < budget:
        print(f"\n✅ You are UNDER budget by ${budget - total_cost:.2f}")
    else:
        print("\n🎯 Your spending matches your budget exactly!")

# === User Inputs ===

print("🌴 Welcome to the Vacation Budget Calculator 🌴\n")

trip_days = int(input("How many days will your trip be? "))
people = int(input("How many people are going? "))
trip_budget = get_positive_float("Enter your total trip budget ($): ")
income = get_positive_float("Enter your monthly income ($): ")

print("\nEnter your estimated trip costs:")

flight_cost = get_positive_float("Total flight cost ($): ")
hotel_cost = get_positive_float("Total hotel cost ($): ")
food_cost = get_positive_float("Total food cost ($): ")
transportation_cost = get_positive_float("Total transportation cost ($): ")

# === Cost Calculations ===

# Store all expenses in a list for flexibility
expenses = [flight_cost, hotel_cost, food_cost, transportation_cost]
total_cost = calculate_total_cost(expenses)
savings = trip_budget - total_cost

# === Results ===

print("\n🔎 Trip Summary:")
print(f"Trip Length: {trip_days} days")
print(f"People Going: {people}")
print(f"Total Trip Cost: ${total_cost:.2f}")
print(f"Savings After Trip: ${savings:.2f}")

# === Budget Evaluation ===
compare_budget(total_cost, trip_budget)

# === Affordability Check ===
if savings >= 0:
    print("✅ You can afford this trip!")
else:
    print("💸 You cannot afford this trip with your current budget.")

