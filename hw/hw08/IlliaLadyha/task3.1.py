from task3 import rectangle_area, triangle_area, circle_area

def main():
    print("Choose the figure to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        # Rectangle
        a = float(input("Enter the length of the rectangle: "))
        b = float(input("Enter the width of the rectangle: "))
        print(f"The area of the rectangle is: {rectangle_area(a, b)}")
    
    elif choice == "2":
        # Triangle
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"The area of the triangle is: {triangle_area(base, height)}")
    
    elif choice == "3":
        # Circle
        radius = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is: {circle_area(radius)}")
    
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        
        
    
    if __name__ == "__main__":
        main()