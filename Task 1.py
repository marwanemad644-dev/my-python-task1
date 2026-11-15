
item1 = 50
item2 = 30
item3 = 20

budget = 120

total_cost = item1 + item2 + item3

print("total cost:", total_cost)
print("budget:", budget)

if total_cost < budget:
    remaining = budget - total_cost
    print("money left:", remaining)

elif total_cost > budget:
    needed = total_cost - budget
    print("more money needed:", needed)

else:
    print("the budget is exactly enough!")