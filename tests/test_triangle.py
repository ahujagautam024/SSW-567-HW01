import pytest

from Triangle import Triangle

# region Invalid Triangle


def test_invalid_triangle():

    with pytest.raises(TypeError, match="All sides must be either integers or floats."):
        Triangle("1", 2, 3)
    
    with pytest.raises(ValueError, match="All sides must be positive numbers."):
        Triangle(-1, 2, 3)
    
    with pytest.raises(ValueError, match="All sides must be positive numbers."):
        Triangle(0, 2, 3)

def test_invalid_triangle_inequality():
    with pytest.raises(ValueError, match="The sum of any two sides must be greater than the third side."):
        Triangle(1, 2, 3)

    with pytest.raises(ValueError, match="The sum of any two sides must be greater than the third side."):
        Triangle(10, 1, 1)

# endregion
        
# region valid examples
        
def test_valid_triangle():
    triangle = Triangle(3, 4, 5)
    assert triangle.side1 == 3
    assert triangle.side2 == 4
    assert triangle.side3 == 5

def test_right_angle():
    triangle = Triangle(3, 4, 5)
    assert triangle.classify_triangle() == "Right angle Triangle"

    triangle2 = Triangle(12, 5, 13)
    assert triangle.classify_triangle() == "Right angle Triangle"

def test_equilateral():
    triangle = Triangle(3, 3, 3)
    assert triangle.classify_triangle() == "Equilateral Triangle"

    triangle2 = Triangle(12, 12, 12)
    assert triangle2.classify_triangle() == "Equilateral Triangle"

def test_isosceles():
    triangle = Triangle(3, 4, 3)
    assert triangle.classify_triangle() == "Isosceles Triangle"

    triangle2 = Triangle(1, 12, 12)
    assert triangle2.classify_triangle() == "Isosceles Triangle"

def test_scalene():
    triangle = Triangle(32, 15, 34)
    assert triangle.classify_triangle() == "Scalene Triangle"

    triangle2 = Triangle(5, 12, 14)
    assert triangle2.classify_triangle() == "Scalene Triangle"

# endregion
