#1que
def check_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        print("valid triangle.")
        # type of triangle
        if a == b == c:
            print("Equilateral triangle")
        elif a == b or b == c or a == c:
            print("Isosceles triangle")
        else:
            print("Scalene triangle")

        #right-angled triangle using Pythagoras Theorem
        sides = sorted([a, b, c])  # Sort the sides
        if sides[0]**2 + sides[1]**2 == sides[2]**2:
            print("It is a Right-angled triangle.")
        else:
            print("It is not a Right-angled triangle.")
    else:
        print("do not form a triangle.")

check_triangle(3, 4, 5) #valid triangle,scalene triangle,right angled triangle
