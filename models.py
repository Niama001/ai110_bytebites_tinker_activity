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

    # Filters menu items and returns only items in the requested category.
    def filterByCategory(self, category):
        matchingItems = []

        for item in self.items:
            if item.category == category:
                matchingItems.append(item)

        return matchingItems

    # Sorts menu items from highest to lowest popularity rating.
    def sortByPopularity(self):
        return sorted(self.items, key=lambda item: item.popularityRating, reverse=True)


class Order:
    def __init__(self):
        self.selectedItems = []
        self.totalCost = 0.0

    # Adds up the price of every selected item and returns the total.
    # An empty order returns 0.0.
    def calculateTotal(self):
        total = 0.0

        for item in self.selectedItems:
            total += item.price

        self.totalCost = total
        return total


# Manual test scenario (only runs when you execute: python models.py)
if __name__ == "__main__":
    # Create sample objects
    burger = MenuItem("Spicy Burger", 10.00, "Entrees", 5)
    soda = MenuItem("Large Soda", 5.00, "Drinks", 3)
    tea = MenuItem("Iced Tea", 3.50, "Drinks", 4)
    brownie = MenuItem("Brownie", 4.00, "Desserts", 2)

    customer = Customer("Alex")
    print("Customer:", customer.name, "| history:", customer.purchaseHistory)
    print("Burger:", burger.name, burger.price, burger.category, burger.popularityRating)

    # Add items to the menu
    menu = Menu()
    menu.items.extend([burger, soda, tea, brownie])

    # Filter by category (expect: Large Soda, Iced Tea)
    drinks = menu.filterByCategory("Drinks")
    print("Drinks:", [item.name for item in drinks])

    # Filter by a category with no items (expect: [])
    print("Snacks:", [item.name for item in menu.filterByCategory("Snacks")])

    # Sort by popularity (expect: Spicy Burger, Iced Tea, Large Soda, Brownie)
    print("By popularity:", [item.name for item in menu.sortByPopularity()])

    # Order total with items (expect: 15.0)
    order = Order()
    order.selectedItems.append(burger)
    order.selectedItems.append(soda)
    print("Order total:", order.calculateTotal())

    # Empty order total (expect: 0.0)
    print("Empty order total:", Order().calculateTotal())

    # Record the order in the customer's history
    customer.purchaseHistory.append(order)
    print("Orders in history:", len(customer.purchaseHistory))