# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop for rows
while row < size:
    # Use for loop to print asterisks in one row
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after one row is printed
    row += 1
