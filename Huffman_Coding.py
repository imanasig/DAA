import heapq

# Build Huffman Tree
def build_tree(text):
    freq = {}

    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    heap = []
    count = 0

    for ch in freq:
        heapq.heappush(heap, (freq[ch], count, ch))
        count += 1

    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)

        new_node = (left, right)

        heapq.heappush(heap, (f1 + f2, count, new_node))
        count += 1

    return heap[0][2]

# Generate Huffman Codes
def generate_codes(root, code, codes):
    if isinstance(root, str):
        codes[root] = code if code else "0"
        return

    generate_codes(root[0], code + "0", codes)
    generate_codes(root[1], code + "1", codes)

# Encode Text
def encode(text, codes):
    result = ""

    for ch in text:
        if ch not in codes:
            return None
        result += codes[ch]

    return result

# Decode Text
def decode(bits, root):
    result = ""

    if isinstance(root, str):
        if any(bit != "0" for bit in bits):
            return None
        return root * len(bits)

    current = root

    for bit in bits:
        if bit == "0":
            current = current[0]
        elif bit == "1":
            current = current[1]
        else:
            return None

        if isinstance(current, str):
            result += current
            current = root

    if current != root:
        return None

    return result

# Main Program
root = None
codes = {}

while True:
    print("\n--- HUFFMAN CODING ---")
    print("1. Build Huffman Tree")
    print("2. Encode Text")
    print("3. Decode Text")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid choice!")
        continue

    if choice == 1:
        text = input("Enter text: ")

        if text == "":
            print("Text cannot be empty!")
            continue

        root = build_tree(text)
        codes = {}
        generate_codes(root, "", codes)

        print("\nHuffman Codes:")
        for ch in codes:
            print(repr(ch), ":", codes[ch])

        print("Huffman Tree built successfully!")

    elif choice == 2:
        if root is None:
            print("Build the tree first!")
            continue

        text = input("Enter text to encode: ")
        result = encode(text, codes)

        if result is None:
            print("Character not found in tree!")
        else:
            print("Encoded Text:", result)

    elif choice == 3:
        if root is None:
            print("Build the tree first!")
            continue

        bits = input("Enter binary text: ")
        result = decode(bits, root)

        if result is None:
            print("Invalid encoded text!")
        else:
            print("Decoded Text:", result)

    elif choice == 4:
        print("Program terminated.")
        break

    else:
        print("Invalid choice!")


# Choice: 1
# Enter text: AAABBC
# Choice: 2
# Enter text to encode: AAABBC
# Decode: Enter the binary string produced by the encode operation.