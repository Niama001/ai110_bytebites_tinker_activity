# Customer: stores customer information and purchase history.
# MenuItem: stores information about a food or drink item.
# Menu: stores the collection of available menu items.
# Order: stores selected items and calculates the order total.

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchaseHistory = []


class MenuItem:
    def __init__(self, name, price, category, popularityRating):
        self.name = name
        self.price = price
        self.category = category
        self.popularityRating = popularityRating


class Menu:
    def __init__(self):
        self.items = []


class Order:
    def __init__(self):
        self.selectedItems = []
        self.totalCost = 0.0

    def calculateTotal(self):
        total = 0.0

        for item in self.selectedItems:
            total += item.price

        self.totalCost = total
        return total