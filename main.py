import math

#input the coordinates of the points
x1 = float(input("Input value of x1:"))
y1 = float(input("Input value of y1:"))
x2 = float(input("Input value of x2:"))
y2 = float(input("Input value of y2:"))

#calculate the distance between the points
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

#display result
print("The distance between of the two points is:", round(distance, 2))

#Reflection question:
#The math library made the program much simpler by providing ready-to-use functions like sqrt() and pow(), which saved time and reduced the need for complex manual calculations. 
#These functions made it easy to perform square roots and exponentiation accurately with just a single line of code. 
#Without them, I would have had to write lengthy algorithms to handle these operations, making the program more complicated and error-prone.
