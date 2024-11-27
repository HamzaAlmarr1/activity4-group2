"""
this script has a class called Polygon
this scrip is the main file because it has the main function
class Polygon makes polygon objects that possess attributes of name(shape) and sides(a list of floats)
"""

class Polygon:

    """
    in this class there is a constructor and the attributes __name and __side has been privated with __slots__
    usage of methods and special methods
    """


    __slots__ = ["__name", "__sides"]
    def __init__(self, name, sides):

        """ 
        constructor with parameters name and sides
        """

        self.__name = name
        self.__sides = sides



     # setters and getters
    def get_name(self):

        """
        method to retrieve name
        """

        return self.__name # returns the name

    def set_name(self, updated_name):

        """
        method to set name
        """

        self.__name = updated_name # returns the updated name
        
    def get_sides(self):

        """
        method to get sides
        """

        return self.__sides # returns the sides
    
    def set_sides(self, updated_sides):

        """
        methods to set sides
        """

        self.__sides = updated_sides # returns the updated sides



    # equality and inequality methods
    def __eq__(self, other):

        """
        special method to check if equality between two objects is true
        """

        return self.__name == other.__name and self.__sides == other.__sides # returns results
    
    def __ne__(self, other):

        """
        special method to check if inequality between two objects is true
        """
        
        return not self.__eq__(other) # returns results
    
    def __str__(self):
        
        """
        special method to return the object as a string represenntation
        """

        return f"{self.__name} with sides: {self.__sides}" # the format of the returned string
    

    def calculate_circumference(self):

        """
        method calculating the circumference of the polygon by summing up the sides
        """

        return sum(_ for _ in self.__sides) # comprehension that uses sum function to itterate and returns the sum of the sides
    


def main():

    """
    the main function; will create three polygon objects, a triangle,square,hexagon with sides
    then prints out a string representation of each of the objects with their circumferences
    """

    # constructing the polygon objects
    triangle = Polygon("triangle", [3.0, 3.0, 3.0])
    square = Polygon("square", [5.0, 5.0, 5.0, 5.0])
    hexagon = Polygon("hexagon", [6.0, 6.0, 6.0, 6.0, 6.0, 6.0])


    # printing the object's string representation and calculated circumference
    print(f"{str(triangle)}\nCircumference: {triangle.calculate_circumference()}") # prints for the triangle
    print(f"\n{str(square)}\nCircumference: {square.calculate_circumference()}") # prints for the square
    print(f"\n{str(hexagon)}\nCircumference: {hexagon.calculate_circumference()}") # prints for the hexagon


if __name__ == "__main__":
    main()