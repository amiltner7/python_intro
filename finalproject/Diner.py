# Aidan Miltner, amiltner@usc.edu
# ITP 115, Spring 2021
# Final Project: Diner Class
# This class will represent a diner at the restaurant - it will monitor their status and their meal

# Import MenuItem class from MenuItem file so that we can use it in our Menu class
from MenuItem import MenuItem


class Diner(object):
    # We have a class variable called "STATUSES" that is a list of the possible statuses the diner can have
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]

    # Constructor (__init__)
    # Inputs/parameters: diner name (str)
    # Output: none
    def __init__(self, dinerName):
        # We have 3 instance attributes. The name attribute will hold the dinerName input, the order attribute will
        # initially be an empty list and we will add items (MenuItem objects) to it as the diner orders, and the status
        # will represent the index of the "STATUSES" variable and initially be 0 (seated).
        self.name = dinerName
        self.order = []
        self.status = 0

    # Get methods for each of the attributes
    def getName(self):
        return self.name

    def getOrder(self):
        return self.order

    def getStatus(self):
        return self.status

    # updateStatus
    # Inputs/parameters: none
    # Output: none
    def updateStatus(self):
        # Increase status (attribute) by 1 (this will represent the diner moving to the next status
        # (ex: seated to ordering)
        self.status += 1

    # addToOrder
    # Inputs/parameters: menuItem object
    # Output: none
    def addToOrder(self, menuItemObject):
        # Adds a menuItem to the end of the order attribute list
        self.order.append(menuItemObject)

    # printOrder
    # Inputs/parameters: none
    # Output: none
    def printOrder(self):
        # Print a message containing everything that was ordered: first we will print a header message including the
        # diner's name (using the name attribute) and "ordered:"
        print("\n" + self.name, "ordered:")
        # Then to print all of the items they ordered we can loop through the order attribute list which contains the
        # menuItem objects that they ordered. We can simply print every one because it is already in a readable format
        # (__self__) in MenuItem.
        for i in self.order:
            print("-", i)

    # getMealCost
    # Inputs/parameters: none
    # Output: total cost of the meal (float)
    def getMealCost(self):
        # We want to add up the prices of each menu item ordered to get a total cost for the meal. First we can
        # initialize a variable for totalCost to 0.0 (float) and then we will add to this variable inside the for loop
        totalCost = 0.0
        # For every item (MenuItem objects representing the items they ordered) in the order attribute list
        for i in self.order:
            # Set a new variable called 'price' (float) to the MenuItem object.getPrice() because this will call the
            # get price function inside the MenuItem class for every item ordered which will return the price.
            price = float(i.getPrice())
            # Then we can add this price to the totalCost variable.
            totalCost += price
        # Once we have done this for every item they ordered, return the total cost of the meal
        return totalCost

    # String (__str__)
    # Input/parameter: none
    # Output: message containing diner's name and status (str)
    def __str__(self):
        # First create a variable called "status" and set the value to the diner's current status. To get the status, we
        # can take the index of their status (stored in status index attribute) within the STATUSES class variable.
        status = Diner.STATUSES[self.status]
        # Then write the string to return. We want to say "Diner" + name (name instance attribute) + "is currently" +
        # status variable from above
        strRepresentation = "Diner " + self.name + " is currently " + status + "."
        # Return the string
        return strRepresentation

