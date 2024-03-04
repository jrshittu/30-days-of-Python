total_cost = 0.0
sugar_tax = 0.5

# Define dictionaries for each type of item
bread_costs = {"Sandwich": 2.00, "Wrap": 2.50}
filling_costs = {"Tuna": 1.50, "Chicken": 2.00}
pudding_costs = {"Cookie": 0.50, "Crisps": 0.75, "Fruit": 1.00, "None": 0.00}
drink_costs = {"Coke": 1.00, "Water": 0.75, "Juice": 0.00}

# Get the user's selection for each type of item
bread_type = input("Sandwich or Wrap?").capitalize()
filling_type = input("Tuna or Chicken?").capitalize()
pudding = input("Cookie, Crisps, Fruit or None?").capitalize()
drink = input("Coke, Water or Juice?").capitalize()

# Add the cost of each selected item to the total cost
total_cost += bread_costs[bread_type]
total_cost += filling_costs[filling_type]
total_cost += pudding_costs[pudding]
total_cost += drink_costs[drink]

# Add the sugar tax to the total cost if the user selected Coke or a Cookie
if drink == "Coke" or pudding == "Cookie":
    total_cost += sugar_tax

# Print the total cost
print(f"Your total cost is £{total_cost}")
