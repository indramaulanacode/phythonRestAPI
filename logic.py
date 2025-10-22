PI = 3.14

radius = 5

def calculate_area(r):
    return PI * r * r
    

for i in range(1,6):
    print ("Number : ", i)

if radius > 0:
    area = calculate_area (radius)
    print ("The area of the circle is ", area)
else:
    print ("Please enter a postive radius ")
 