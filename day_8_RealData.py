numbers = [12, 345, 2, 6, 7896, 4567, 890, 1234, 99]
even_digit_count = 0
for num in numbers:

    
    digit_count = len(str(num))

    # Check if digit count is even
    if digit_count % 2 == 0:
        even_digit_count += 1


print("User Data Array:", numbers)
print("Numbers with even number of digits:", even_digit_count)


print("\nExplanation:")
print("Arrays are used in real systems to store and process large amounts of data efficiently.")
print("Examples include analytics dashboards, logs processing, and user activity tracking.")