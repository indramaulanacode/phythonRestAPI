# Constants
PI = 3.14

# Variables
radius = 5

# Function to calculate the area of a circle
def calculate_area(radius):
    return PI * radius * radius

# Loop to print numbers from 1 to 5
for i in range(1, 6):
    print("Number:", i)

# Condition to check if radius is positive
if radius > 0:
    area = calculate_area(radius)
    print("The area of the circle is", area)
else:
    print("Please enter a positive radius")