# Aidan Miltner, amiltner@usc.edu
# ITP 115, Spring 2021
# Final Project: MenuItem Class
# This class will represent a single item on the menu - its name, category, price, and description, and return these
# attributes in a readable format.

class MenuItem(object):
    # Constructor (__init__)
    # Inputs/parameters: name (str), category (str), price (float), description (str)
    # No output
    def __init__(self, nameVal, categoryVal, priceVal, descVal):
        # I will assign each of the inputs to the 4 instance attributes. Need to make the priceVal a float.
        self.name = nameVal
        self.category = categoryVal
        self.price = float(priceVal)
        self.desc = descVal

    # Define get methods for each of the attributes
    def getName(self):
        return self.name

    def getCategory(self):
        return self.category

    def getPrice(self):
        return self.price

    def getDesc(self):
        return self.desc

    # String method (__str__)
    # Inputs/parameters: none
    # Output: A string that includes all of the attributes in a menu format
    def __str__(self):
        # String to return: <name> (<category>): <price>
        #                       <description>
        return self.name + " (" + self.category + "): $" + str(self.price) + "\n     " + self.desc

