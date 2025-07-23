trip_days = 7
people = 4
trip_budget = 8000.00
income = 100000.00
flight_cost = 2400.00
hotel_cost = 2400.00
food_cost = 300.00
transportation_cost = 0

flight_cost = float(input("Enter total flight cost $"))
hotel_cost = float(input("Enter total hotel cost $"))
food_cost = float(input("Enter total food cost $"))
transportation_cost = float(input("Enter total transportation cost $"))

total_expenses = flight_cost + hotel_cost + food_cost + transportation_cost
print("Trip budget: ${:.2f}".format(trip_budget))
print("Total expenses: ${:.2f}".format(total_expenses))

if total_expenses <= trip_budget:
    print("✅ You're within budget!")
else: 
    print("❌ You're over budget by ${:.2f}".format(total_expenses - trip_budget))

savings = income - trip_budget

