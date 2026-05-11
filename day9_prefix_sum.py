arr = [2, 4, 1, 7, 3, 6, 5]

prefix = [0] * len(arr)

prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]

print("Original Array:", arr)
print("Prefix Sum Array:", prefix)

def brute_force_sum(left, right):
    total = 0

    for i in range(left, right + 1):
        total += arr[i]

    return total

def prefix_sum_query(left, right):

    if left == 0:
        return prefix[right]

    return prefix[right] - prefix[left - 1]


queries = [(0, 3), (2, 5), (1, 6)]

print("\nQuery Results:\n")

for left, right in queries:

    brute = brute_force_sum(left, right)
    optimized = prefix_sum_query(left, right)

    print(f"Range ({left} to {right})")
    print("Brute Force Sum:", brute)
    print("Optimized Sum :", optimized)
    print()