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
#The math library was a huge time-saver. Instead of writing long, 
#bug-prone code to calculate square roots and powers from scratch, 
#I could just use sqrt() and pow() to keep things clean and accurate
