from Triangle import Triangle

if __name__ == "__main__":

    try:
        triangle = Triangle(1,2,3)
        triangle.display_sides()
        print(triangle.classifyTriangle())
    except ValueError as error:
        print(f"Error: {error}")