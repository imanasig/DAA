class Item:
    """Class representing an item with value, weight, and value/weight ratio."""
    def __init__(self, item_id, value, weight):
        self.id = item_id
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(items, capacity):
    """
    Solves Fractional Knapsack problem using Greedy approach.
    Returns the maximum total value that can be put in the knapsack.
    """
    # Step 1: Sort items by value-to-weight ratio in descending order (Greedy choice)
    items.sort(key=lambda x: x.ratio, reverse=True)

    print("\n--- Items Sorted by Ratio (Value / Weight) in Descending Order ---")
    for item in items:
        print(f"Item {item.id}: Value = {item.value}, Weight = {item.weight}, Ratio = {item.ratio:.2f}")

    total_value = 0.0
    remaining_capacity = capacity

    print("\n--- Items Selected in Knapsack ---")
    for item in items:
        if remaining_capacity <= 0:
            break

        if item.weight <= remaining_capacity:
            # Take the full item
            total_value += item.value
            remaining_capacity -= item.weight
            print(f"Item {item.id}: 100% taken -> Added weight: {item.weight}, Added value: {item.value}")
        else:
            # Take a fraction of the item to fill the remaining capacity
            fraction = remaining_capacity / item.weight
            added_value = item.value * fraction
            total_value += added_value
            print(f"Item {item.id}: {fraction * 100:.2f}% taken -> Added weight: {remaining_capacity}, Added value: {added_value:.2f}")
            remaining_capacity = 0

    return total_value

def main():
    print("=== Fractional Knapsack Problem (Greedy Method) ===")
    n = int(input("Enter number of items: "))

    if n <= 0:
        print("Number of items must be greater than 0.")
        return

    items = []
    for i in range(n):
        print(f"\nItem {i + 1}:")
        value = float(input("  Enter value (profit): "))
        weight = float(input("  Enter weight: "))
        
        if weight <= 0:
            print("Weight must be greater than 0. Skipping item.")
            continue
        
        items.append(Item(i + 1, value, weight))

    if not items:
        print("No valid items entered.")
        return

    capacity = float(input("\nEnter maximum knapsack capacity: "))
    if capacity <= 0:
        print("Capacity must be greater than 0.")
        return

    max_value = fractional_knapsack(items, capacity)
    print(f"\nMaximum value in knapsack = {max_value:.2f}")

main()


# Test Case 1: Normal execution 
# Enter number of items: 3
# Item 1:
# Enter value (profit): 60
# Enter weight: 10
# Item 2:
# Enter value (profit): 100
# Enter weight: 20
# Item 3:
# Enter value (profit): 120
# Enter weight: 30
# Enter maximum knapsack capacity: 50

# Test Case 2: All items fit completely
# Enter number of items: 3
# Item 1:
# Enter value (profit): 10
# Enter weight: 2
# Item 2:
# Enter value (profit): 20
# Enter weight: 3
# Item 3:
# Enter value (profit): 30
# Enter weight: 4
# Enter maximum knapsack capacity: 20