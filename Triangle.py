class Triangle:
    def __init__(self, side1, side2, side3):

        if not all(isinstance(side, (int, float)) for side in (side1, side2, side3)):
            raise TypeError("All sides must be either integers or floats.")

        if not (side1 > 0 and side2 > 0 and side3 > 0):
            raise ValueError("All sides must be positive numbers.")
        
        if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
            raise ValueError("The sum of any two sides must be greater than the third side.")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def display_sides(self):
        print(f"Sides of the triangle are: {self.side1}, {self.side2}, {self.side3}")
    
    def is_right_angle(self):
        a, b, c = sorted([self.side1, self.side2, self.side3])
        return a**2 + b**2 == c**2

    def classify_triangle(self):
        if (self.side1 == self.side2 == self.side3):
            return 'Equilateral Triangle'
        elif self.side1 == self.side2 or self.side2 == self.side3 or self.side1 == self.side3:
            return 'Isosceles Triangle'
        elif self.is_right_angle():
            return 'Right angle Triangle'
        else:
            return 'Scalene Triangle'