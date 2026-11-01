import time

# ---------- Recursive Fibonacci ----------
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# ---------- Non-Recursive Fibonacci ----------
def fib_non_recursive(n):
    n1, n2 = 0, 1

    for i in range(n):
        print(n1, end=" ")
        n1, n2 = n2, n1 + n2

    print()

# ---------- Recursive Tower of Hanoi ----------
def tower_of_hanoi(n, source, auxiliary, destination, move_count):
    if n == 0:
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary, move_count)

    move_count[0] += 1
    print(f"Move disk {n} from {source} to {destination}")

    tower_of_hanoi(n - 1, auxiliary, source, destination, move_count)

# ---------- Main Function ----------
def main():

    # ----- Fibonacci Section -----
    try:
        n = int(input("Enter number of Fibonacci terms: "))

        if n < 0 or n > 35:
            print("Enter a number between 0 and 35.")
            return

        print("\nFibonacci Sequence (Recursive): ", end="")
        start1 = time.perf_counter()

        for i in range(n):
            print(fib_recursive(i), end=" ")

        end1 = time.perf_counter()
        time_recursive = (end1 - start1) * 1_000_000

        print("\n\nFibonacci Sequence (Non-Recursive): ", end="")
        start2 = time.perf_counter()

        fib_non_recursive(n)

        end2 = time.perf_counter()
        time_nonrecursive = (end2 - start2) * 1_000_000

        print("\n=== Fibonacci Complexity Analysis ===")
        print(f"Recursive Time Taken: {time_recursive:.2f} microseconds")
        print("Recursive Time Complexity: O(2^n)")
        print("Recursive Space Complexity: O(n)")

        print(f"\nNon-Recursive Time Taken: {time_nonrecursive:.2f} microseconds")
        print("Non-Recursive Time Complexity: O(n)")
        print("Non-Recursive Space Complexity: O(1)")

        # ----- Tower of Hanoi Section -----
        print("\n=== Tower of Hanoi ===")
        disks = int(input("Enter number of disks: "))

        if disks < 0 or disks > 15:
            print("Enter a number between 0 and 15.")
            return

        move_count = [0]

        start3 = time.perf_counter()

        tower_of_hanoi(disks, 'A', 'B', 'C', move_count)

        end3 = time.perf_counter()
        time_hanoi = (end3 - start3) * 1_000_000

        print("\n=== Tower of Hanoi Complexity Analysis ===")
        print(f"Total Moves: {move_count[0]}")
        print(f"Expected Moves: {2**disks - 1}")
        print(f"Time Taken: {time_hanoi:.2f} microseconds")
        print("Time Complexity: O(2^n)")
        print("Space Complexity: O(n)")

    except ValueError:
        print("Invalid input! Enter an integer.")


main()

#Fibonacci terms: 7

#Hanoi disks: 3

