# Aidan Miltner, amiltner@usc.edu
# ITP 115, Spring 2021
# Final Project: Menu Class
# This class will contain the full menu and be able to get menu items, the number of items, and print out the menu.

# Import MenuItem class from MenuItem file so that we can use it in our Menu class
from MenuItem import MenuItem


class Menu(object):
    # We have a class variable called "CATEGORIES" that is a list containing the possible categories of menu items
    CATEGORIES = ["Drink", "Appetizer", "Entree", "Dessert"]

    # Constructor (__init__)
    # Inputs/parameters: name of csv file (str) that has information about the menu (menu.csv)
    # Output: none
    def __init__(self, fileName):
        # Each of the instance attributes will initially be an empty list. We will add to these lists as we get our
        # menu items
        self.drinks = []
        self.appetizers = []
        self.entrees = []
        self.desserts = []

        # We first want to open a connection to the csv file that we inputted (will be menu.csv), and read it ("r").
        fileConnection = open(fileName, "r")
        # For every line in the csv file (each menu item is on its own line in the file so we need to loop through all
        # of them):
        for line in fileConnection:
            # We need to strip the line because each line contains a new line at the end so we must remove this space
            # using the .strip() function.
            strippedLine = line.strip()
            # Now we want to split the line using the .split() function to create a list for each menu item. I will
            # store this in a variable called 'lineList', and the delimiter will be a comma (',') because the name,
            # category, price, and description for each menu item are separated by commas.
            lineList = strippedLine.split(",")
            # Now we can create a menu item object because we have each menu item's name (index 0 in lineList),
            # category (index 1 in lineList), price (index 2 in lineList) , and description (index 3 in lineList)
            menuItemObject = MenuItem(lineList[0], lineList[1], lineList[2], lineList[3])
            # Finally I need to assign each menu item to one of the category lists (instance attributes) so we need
            # to check the category for each item (index 1 in lineList). Depending on which category it is in, I will
            # append that category's list to add the menuItemObject (which will be a string containing the
            # characteristics of the item in a readable format (that we created in our __str__ part of the menuItem
            # class)
            # Maybe use CATEGORIES[1] instead of "Appetizer"??
            if lineList[1] == "Appetizer":
                self.appetizers.append(menuItemObject)
            elif lineList[1] == "Drink":
                self.drinks.append(menuItemObject)
            elif lineList[1] == "Entree":
                self.entrees.append(menuItemObject)
            elif lineList[1] == "Dessert":
                self.desserts.append(menuItemObject)

        # Close the file
        fileConnection.close()

    # getMenuItem
    # Inputs/parameters: category (str), index position of certain menu item (int)
    # Output: MenuItem object from correct instance attribute
    def getMenuItem(self, category, index):
        # First need to make sure that the category input is an actual category - to do this we can set an if statement
        # to ensure that the capitalized category is in the CATEGORIES list (our class variable containing all of the
        # possible categories)
        if category.capitalize() in Menu.CATEGORIES:
            # Depending on what the category is, assign a variable named 'cat' (category) to the instance attribute
            # associated with that category (list containing MenuItem objects for that category).
            if category.capitalize() == "Drink":
                cat = self.drinks
            elif category.capitalize() == "Appetizer":
                cat = self.appetizers
            elif category.capitalize() == "Entree":
                cat = self.entrees
            elif category.capitalize() == "Dessert":
                cat = self.desserts

            # If the index input (int) is between 0 and the length of the 'cat' list (list containing MenuItem objects
            # for the specified category), then return the MenuItem object by returning the item at the specified
            # index. If it is not in the range of the appropriate list, then nothing will be returned
            if 0 <= int(index) < len(cat):
                return cat[index]
        # else:
        #     return

    # printMenuItems
    # Inputs/parameters: category (str)
    # Outputs: none
    def printMenuItems(self, category):
        # Similar to above, first check that the category is an actual category (in the CATEGORIES list)
        if category.capitalize() in Menu.CATEGORIES:
            # Same as above, assign a new variable called 'catList' to one of the instance attributes depending on what
            # the inputted category is
            if category.capitalize() == "Drink":
                catList = self.drinks
            elif category.capitalize() == "Appetizer":
                catList = self.appetizers
            elif category.capitalize() == "Entree":
                catList = self.entrees
            elif category.capitalize() == "Dessert":
                catList = self.desserts
            # Now instead of returning the MenuItem, we will print out the menu items. First, print the category name
            # with lines around it
            print("\n-----" + category.upper() + "S-----")
            # Then, for every index in the 'catList' (list containing menuItem objects), print the number of the index
            # with a ')' (ex: 0), 1), etc), as well as the menuItem object at that index (this will be the item in a
            # readable format (what we wrote in our __str__ for MenuItem). Use range() to do this, starting at 0 index
            # and going through the length of the list
            for i in range(0, len(catList)):
                print(str(i) + ")", catList[i])
        # If it is not a valid category, print nothing
        else:
            print("")

    # getNumMenuItems
    # Inputs/parameters: category (str)
    # Outputs: number of MenuItems in the category
    def getNumMenuItems(self, category):
        # Same as above
        if category.capitalize() in Menu.CATEGORIES:
            # Same as above
            if category.capitalize() == "Drink":
                catList = self.drinks
            elif category.capitalize() == "Appetizer":
                catList = self.appetizers
            elif category.capitalize() == "Entree":
                catList = self.entrees
            elif category.capitalize() == "Dessert":
                catList = self.desserts
            # This time return the length of the 'catList' using len()
            return len(catList)
        # If it is not a valid category, return 0
        else:
            return 0

