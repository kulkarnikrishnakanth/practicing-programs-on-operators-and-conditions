
length = float(input("enter length: "))
breadth = float(input("enter breadth: "))
if length == breadth:
    print("it is square")
    area = length ** 2
    print("area of the square is:",area)
else:
    print("it is rectangle")
    area = length * breadth
    print("area of the rectangle is:",area)
