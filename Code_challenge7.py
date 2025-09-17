print("ODD NUMBER ACCUMULATOR")
print("Enter 10 numbers. We'll sum only the odd ones!")

odd_sum = 0
for i in range(1, 11):
    while True:
        try:
            num = int(input(f"Enter number {i}: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    if num % 2 != 0:
        odd_sum += num

print("\nSum of all odd numbers:", odd_sum)
