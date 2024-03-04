total_cost = 0.0
sugar_tax = 0.5

bread_type = input("Sandwich or Wrap?").capitalize()
filling_type = input("Tuna or Chicken?").capitalize()
pudding = input("Cookie, Crisps, Fruit or None?").capitalize()
drink = input("Coke, Water or Juice?").capitalize()

# Add cost for bread_type
if bread_type == "Sandwich":
    total_cost += 2.00
else:
    total_cost += 2.50

# Add cost for filling type
if filling_type == "Tuna":
    total_cost += 1.50
else:
    total_cost += 2.00

# add cost for pudding type
if pudding == "Cookie":
    total_cost += 0.50
    total_cost += sugar_tax
elif pudding == "Crisps":
    total_cost += 0.75
elif pudding == "Fruit":
    total_cost += 1.00
else:
    total_cost += 0.00

if drink == "Coke":
    total_cost += 1.00
    total_cost += sugar_tax
elif drink == "Water":
    total_cost += 0.75
else:
    total_cost += 0.0

# print
print(f"Your total cost is £{total_cost}")