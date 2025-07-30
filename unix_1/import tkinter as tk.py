import tkinter as tk
from tkinter import messagebox

# === Your Existing Variables and Functions (unchanged) ===
trip_days = 7
people = 4
trip_budget = 8000.00
income = 100000.00
flights = 2400.00
hotel = 2400.00
food = 2100.00
transportation = 0

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

def calculate_total(expenses):
    total = 0
    for item in expenses:
        total += item["cost"][0]
    return total

def print_expense_breakdown(expenses):
    print("\n--- Expense Breakdown ---")
    for item in expenses:
        category = item["category"]
        total = item["cost"][0]
        per_person = item["cost"][1]
        print(f"- {category}: Total = ${total:.2f}, Per Person = ${per_person:.2f}")


# === New: GUI Implementation ===

def run_budget_calculator():
    try:
        # Get user input from GUI
        flight_cost = float(flight_entry.get())
        hotel_cost = float(hotel_entry.get())
        food_cost = float(food_entry.get())

        # Organize expenses
        expenses = [
            {"category": "Flight", "cost": (flight_cost, flight_cost / people)},
            {"category": "Hotel", "cost": (hotel_cost, hotel_cost / people)},
            {"category": "Food", "cost": (food_cost, food_cost / people)},
        ]

        # Calculate totals
        total_expenses = calculate_total(expenses)
        savings = income - trip_budget

        # Summary message
        summary = "\n--- Vacation Budget Summary ---\n"
        summary += f"Trip Budget:      ${trip_budget:.2f}\n"
        summary += f"Total Expenses:   ${total_expenses:.2f}\n"

        if total_expenses <= trip_budget:
            summary += "✅ You're within budget!\n"
        else:
            over = total_expenses - trip_budget
            summary += f"❌ You're over budget by ${over:.2f}\n"

        summary += f"Estimated Savings After Budget: ${savings:.2f}\n"

        if savings >= total_expenses:
            summary += "🎉 You can afford this trip comfortably!\n"
        else:
            summary += "⚠️ You need to save more to afford this trip.\n"

        # Print breakdown to terminal
        print_expense_breakdown(expenses)

        # Show result in popup
        messagebox.showinfo("Budget Result", summary)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers only.")


# === GUI Layout ===
window = tk.Tk()
window.title("Vacation Budget Calculator")
window.geometry("400x300")

tk.Label(window, text="Enter Total Flight Cost ($):").pack()
flight_entry = tk.Entry(window)
flight_entry.pack()

tk.Label(window, text="Enter Total Hotel Cost ($):").pack()
hotel_entry = tk.Entry(window)
hotel_entry.pack()

tk.Label(window, text="Enter Total Food Cost ($):").pack()
food_entry = tk.Entry(window)
food_entry.pack()

tk.Button(window, text="Calculate Budget", command=run_budget_calculator).pack(pady=10)

# Run the GUI loop
window.mainloop()
