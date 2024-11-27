"""
this scrip will be used to test the following functionalities from polygon:
the initilization
the equality
the inequality
the string representation
the calculated circumference

import from pytest for calculation purposes
"""


from polygon import Polygon
import pytest


def test_polygon_initialization():

    """
    testing the initlization from polygon and verifying with assert statements
    """



    # testing getters from Polygon: get_name, get_sides
    polygon1 = Polygon("Sqaure", [2.0, 2.0, 2.0, 2.0])

    assert polygon1.get_name() == "Square"  # verifying if get_name is correct
    assert polygon1.get_sides() == [2.0, 2.0, 2.0, 2.0]  #verifying if get_sides is correct

    
    # testing setters from Polygon: set_name, set_sides


    updated_polygon_name = "Hexagon"
    polygon1.set_name(updated_polygon_name)
    assert polygon1.get_name() == updated_polygon_name  #verifying if set_name worked and is correct

    updated_polygon_sides = [4.0, 4.0, 4.0, 4.0, 4.0, 4.0]
    polygon1.set_sides(updated_polygon_sides)
    assert polygon1.get_sides() == updated_polygon_sides  #verifying if set_sides worked and is correct



def test_polygon_equality():

    """
    testing the equality method on the polygons and verifying with an assert statement
    """

    # testing the __eq__ method on Polygon
    polygon2 = Polygon("Triangle", [7.0, 7.0, 7.0])
    polygon3 = Polygon("Triangle", [7.0, 7.0, 7.0])

    assert polygon2.__eq__(polygon3) == True


def test_polygon_inequality():

    """
    testing the inequality method on the polygons and verifying it with an assert statement
    """

    # testing the __ne__ method on Polygon
    polygonH = Polygon("Hexagon", [4.0, 4.0, 4.0, 4.0, 4.0, 4.0])
    polygonT = Polygon("Triangle", [3.0, 3.0, 3.0])

    assert polygonH.__ne__(polygonT) == True



def test_polygon_str():

    """
    testing to verify the if the string representation of the polygon by using a assert statement
    """
    
    #
    polygon1 = Polygon("Square", [2.0, 2.0, 2.0, 2.0])
    assert str(polygon1) == "Square with sides: [2.0, 2.0, 2.0, 2.0]"




def test_calculate_circumference():

    """
    testing the calculate_circumference function from polygon and checking if the results are accurate with an assert statements
    """

    #calculating and verifying the following polygon objects circumferences
    hexagon = Polygon("Hexagon", [2.0, 2.0, 2.0, 2.0, 2.0, 2.0])
    hexagon_circumference = hexagon.calculate_circumference()
    assert hexagon_circumference == pytest.approx(12.0)
    
    
    triangle = Polygon("Triangle", [5.0, 5.0, 5.0,])
    triangle_circumference = triangle.calculate_circumference()
    assert triangle_circumference == pytest.approx(15.0)

