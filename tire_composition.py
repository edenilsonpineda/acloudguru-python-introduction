from math import pi

"""
@author: edenilsonpineda
@date: 21-02-2022
"""


class Tire:

    def __init__(self, tire_type, width, ratio, diameter, brand='', construction='R'):
        self.tire_type = tire_type
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand
        self.construction = construction

    def circumference(self):
        """
        The circumference of the tire in inches

        Call this test with:
        python3.7 -m doctest -v {filename.py}

        >>> tire = Tire('P',205,65,15)
        >>> tire.circumference()
        80.1
        """
        side_wall_inches = (self.width * (self.ratio / 100)) / 25.4
        total_diameter = side_wall_inches * 2 + self.diameter
        return round(total_diameter * pi, 1)

    def __repr__(self):
        """
        Represent the tire's information in the standard notation
        present on the side of the tire

        Example: 'P215/65R15'
        :return: string
        """
        return (f"{self.tire_type}{self.width}/{self.ratio}"
                + f"{self.construction}{self.diameter}")
