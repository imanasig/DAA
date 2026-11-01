# 0/1 Knapsack using Dynamic Programming

def print_dp_table(dp):
    print("\n--- DP Table ---")

    for row in dp:
        for val in row:
            print(val, end="\t")
        print()


def knapsack(weights, values, capacity):

    n = len(values)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    print_dp_table(dp)

    # Find selected items
    selected = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i)
            w -= weights[i - 1]

    selected.reverse()

    return dp[n][capacity], selected


# Main Program
print("=== 0/1 Knapsack - Dynamic Programming ===")

try:
    n = int(input("Enter number of items: "))

    if n <= 0:
        print("Number of items must be positive.")
        exit()

    values = []
    weights = []

    for i in range(n):
        print("\nItem", i + 1)

        val = int(input("Enter value: "))
        wt = int(input("Enter weight: "))

        if val < 0 or wt <= 0:
            print("Invalid value or weight!")
            exit()

        values.append(val)
        weights.append(wt)

    capacity = int(input("\nEnter knapsack capacity: "))

    if capacity < 0:
        print("Capacity cannot be negative.")
        exit()

    max_profit, selected = knapsack(weights, values, capacity)

    print("\n--- RESULT ---")
    print("Maximum Profit:", max_profit)

    if selected:
        print("Selected Items:", selected)
    else:
        print("No items selected.")

    total_weight = sum(weights[i - 1] for i in selected)

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