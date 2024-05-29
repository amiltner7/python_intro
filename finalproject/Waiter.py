# Aidan Miltner, amiltner@usc.edu
# ITP 115, Spring 2021
# Final Project: Waiter class
# This class will represent a waiter at the restaurant so will have lots of functionality. The class will hold a list of
# all diners and progress the diner through the statuses by printing the menu, taking their order, printing the meal
# cost, and advancing and removing diners.

# Import Menu and Diner classes from Menu.py and Diner.py so that we can utilize them throughout the class
from Menu import Menu
from Diner import Diner


class Waiter(object):
    # Constructor (__init__)
    # Inputs/parameters: Menu object
    # Output: None
    def __init__(self, menuObject):
        # The diner instance attribute will initially be an empty list because there are no diners. Diners will be added
        # as they arrive. The menu instance attribute will hold a menuObject to represent the menu
        self.diners = []
        self.menu = menuObject

    # addDiner
    # Inputs/parameters: Diner object
    # Output: None
    def addDiner(self, dinerObject):
        # Take the inputted Diner object and add it to the diners instance attribute list using .append()
        self.diners.append(dinerObject)

    # getNumDiners
    # Inputs/parameters: None
    # Output: Number of diners the waiter is currently keeping track of (int)
    def getNumDiners(self):
        # Return the number of diners currently being taken care of (the length of the diners instance attribute)
        return len(self.diners)

    # printDinerStatuses
    # Inputs/parameters: None
    # Output: None
    def printDinerStatuses(self):
        # We want to print all of the diners separated by their status. So, first I will print "Diners who are ___"
        # where __ is each possible status (seated, ordering, etc.).
        print("Diners who are seated:")
        # For every diner (Diner object) in the diners instance attribute list...
        for i in self.diners:
            # I will use the getStatus() function from the Diner class to get the index of the status of that diner and
            # store it in a variable called 'statusIndex'
            statusIndex = i.getStatus()
            # Then I need to get the actual status, so I will take the statusIndex of the STATUSES class variable within
            # the diner class (make sure to do Diner.STATUSES and not just STATUSES), store it in variable 'status'
            status = Diner.STATUSES[statusIndex]
            # Then if that status is "seated" (or whatever status I am printing above), print the Diner (note this will
            # print what we wrote in the __str__ function within the Diner class).
            if status == "seated":
                print("    ", i)
        # Same process as above for each of the statuses...
        print("Diners who are ordering:")
        for i in self.diners:
            statusIndex = i.getStatus()
            status = Diner.STATUSES[statusIndex]
            if status == "ordering":
                print("    ", i)
        print("Diners who are eating:")
        for i in self.diners:
            statusIndex = i.getStatus()
            status = Diner.STATUSES[statusIndex]
            if status == "eating":
                print("    ", i)
        print("Diners who are paying:")
        for i in self.diners:
            statusIndex = i.getStatus()
            status = Diner.STATUSES[statusIndex]
            if status == "paying":
                print("    ", i)
        print("Diners who are leaving:")
        for i in self.diners:
            statusIndex = i.getStatus()
            status = Diner.STATUSES[statusIndex]
            if status == "leaving":
                print("    ", i)

    # takeOrders
    # Inputs/parameters: None
    # Output: None
    def takeOrders(self):
        # Loop through every diner (Diner object) in the diners instance attribute
        for i in self.diners:
            # Same as above to get the status of that diner
            statusIndex = i.getStatus()
            status = Diner.STATUSES[statusIndex]
            # Check if the status is "ordering"
            if status == "ordering":
                # If they are ordering, we need to print the menu and get the diner's selections for what they want to
                # order. So, loop through every category (CATEGORIES class variable in Menu class).
                for cat in Menu.CATEGORIES:
                    # We can use the menu instance attribute which holds a Menu object and use the .printMenuItems
                    # function within the Menu class. Our input is the category, which will be the current category
                    # we are looping through
                    self.menu.printMenuItems(cat)
                    # Once the menu is printed for that category, we want to print a message asking the diner to select
                    # a menu item. We can use i (Diner object within the diners list) and the .getName() function within
                    # the Diner class to get the name of the diner, and then "please select a", <current category
                    # looping through>, "menu item number."
                    print(i.getName() + ", please select a " + cat + " menu item number.")
                    # We need to make sure they enter a valid choice, so we can use a while loop to keep looping until
                    # they enter a valid number. First set a new variable called 'choice' to -1 to make the while loop
                    # run at least once.
                    choice = -1
                    # While the 'choice' variable (int) is negative or greater than the number of items in the current
                    # category's list of menu items (use menu.getNumMenuItems with current category as input) -1
                    # (because there is one less index than the number of items in the list), keep asking the diner for
                    # a choice.
                    while int(choice) < 0 or int(choice) > int(self.menu.getNumMenuItems(cat)-1):
                        choice = int(input("> "))
                    # Once they input a valid choice, we want to get that item. We can do this by calling the
                    # getMenuItem() function from the Menu class. Use menu instance attribute and the category and
                    # choice (index) as inputs. Store this in 'item' variable.
                    item = self.menu.getMenuItem(cat, choice)
                    # Now that we have the item, add it to the order. Do this by calling the Diner class (i) and the
                    # .addToOrder() function within the diner class with the item as the input.
                    i.addToOrder(item)
                # Now print the order using the printOrder() function from the Diner class so that we know what the
                # diner ordered
                i.printOrder()

    # printMealCost
    # Inputs/parameters: None
    # Output: None
    def printMealCost(self):
        # Similarly to above, loop through all of the Diner objects within the diners instance attribute list
        for i in self.diners:
            # Get the status the same way as above
            statusIndex = i.getStatus()
            status = Diner.STATUSES[statusIndex]
            # Now check if the status is "paying"
            if status == "paying":
                # If it is, call the .getMealCost() function from the Diner class using the diner object (i) and make it
                # a float
                cost = float(i.getMealCost())
                # Then print out the total meal cost to the diner (we can use the .getName() function also within the
                # Diner class to get the diner's name).
                print("\n" + i.getName() + ", your meal cost is $" + str(cost))

    # removeDiners
    # Input/parameters: None
    # Output: None
    def removeDiners(self):
        # Once the diner has gone through all of the statuses (is at 'leaving' status), we want to remove them from the
        # list of diners. We must loop through every diner, check their status, and remove them if they are at 'leaving'
        # status. To do this, we need to loop through the diners list backwards to ensure we do not miss anyone. So,
        # use a range-based for loop with the range starting at the last index (length of the diners list - 1), ending
        # at 0 (type -1 because range stops 1 index before value), with step = -1.
        for index in range(len(self.diners)-1, -1, -1):
            # Get the diner at the index
            diner = self.diners[index]
            # Get the status like we have done above
            statusIndex = diner.getStatus()
            status = diner.STATUSES[statusIndex]
            # If their status is "leaving"
            if status == "leaving":
                # Print a message thanking the diner (note: use .getName() function from Diner class again to get their
                # name).
                print("\n" + diner.getName() + ", thank you for dining with us! Come again soon!")
                # Remove the diner from the diners list
                self.diners.remove(diner)

    # advanceDiners
    # Input/parameters: None
    # Output: None
    def advanceDiners(self):
        # Finally, we need to call all of the functions above to progress diners through the restaurant. First print the
        # diner statuses using .printDinerStatuses(self) function.
        Waiter.printDinerStatuses(self)
        # Next take orders using .takeOrders(self) function.
        Waiter.takeOrders(self)
        # Next print the total cost using .printMealCost(self) function.
        Waiter.printMealCost(self)
        # Next remove the diner from the diners list using .removeDiners(self) function
        Waiter.removeDiners(self)
        # Finally call the updateStatus() function from the Diner class using diner object ('diner') so that the diners
        # progress 1 index (status) every time.
        for diner in self.diners:
            diner.updateStatus()

