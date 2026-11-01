# 0/1 Knapsack using Branch and Bound

def bound(items, i, weight, profit, capacity):

    total = weight
    result = profit

    while i < len(items) and total + items[i][2] <= capacity:
        total += items[i][2]
        result += items[i][1]
        i += 1

    if i < len(items):
        remaining = capacity - total
        result += remaining * items[i][3]

    return result


def knapsack(items, capacity):

    items.sort(key=lambda x: x[3], reverse=True)

    best_profit = 0
    best_items = []

    def solve(i, weight, profit, selected):
        nonlocal best_profit, best_items

        if profit > best_profit:
            best_profit = profit
            best_items = selected.copy()

        if i == len(items):
            return

        # Calculate upper bound
        if bound(items, i, weight, profit, capacity) <= best_profit:
            return

        item_id, value, wt, ratio = items[i]

        # Include item
        if weight + wt <= capacity:
            selected.append(item_id)

            solve(i + 1, weight + wt,
                  profit + value, selected)

            selected.pop()

        # Exclude item
        solve(i + 1, weight, profit, selected)

    solve(0, 0, 0, [])

    return best_profit, sorted(best_items)


# Main Program
print("=== 0/1 Knapsack - Branch and Bound ===")

try:
    n = int(input("Enter number of items: "))

    if n <= 0:
        print("Number of items must be positive.")
        exit()

    items = []
    values = []
    weights = []

    for i in range(n):
        print("\nItem", i + 1)

        value = int(input("Enter value: "))
        weight = int(input("Enter weight: "))

        if value < 0 or weight <= 0:
            print("Invalid value or weight!")
            exit()

        ratio = value / weight

        items.append((i + 1, value, weight, ratio))
        values.append(value)
        weights.append(weight)

    capacity = int(input("\nEnter knapsack capacity: "))

    if capacity < 0:
        print("Capacity cannot be negative.")
        exit()

    max_profit, selected = knapsack(items, capacity)

    total_weight = sum(weights[i - 1] for i in selected)

    print("\n--- RESULT ---")
    print("Maximum Profit:", max_profit)
    print("Selected Items:", selected)
    print("Total Weight:", total_weight)
    print("Knapsack Capacity:", capacity)

except ValueError:
    print("Invalid input! Enter integer values.")


#Test Case 1: Normal input
#Enter number of items: 3
# Item 1
# Enter value: 60
# Enter weight: 10
# Item 2
# Enter value: 100
# Enter weight: 20
# Item 3
# Enter value: 120
# Enter weight: 30
# Enter knapsack capacity: 50

# Test Case 4: All items fit
# Number of items: 3
# Item 1
# Value: 10
# Weight: 2
# Item 2
# Value: 20
# Weight: 3
# Item 3
# Value: 30
# Weight: 4
# Capacity: 20