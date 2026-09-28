from models import Customer, MenuItem, Menu, Order


# Test 1: Order total with multiple items
# A $10 burger and a $5 soda in one order should total $15.
def test_calculate_total_with_multiple_items():
    burger = MenuItem("Spicy Burger", 10.00, "Entrees", 5)
    soda = MenuItem("Large Soda", 5.00, "Drinks", 3)

    order = Order()
    order.selectedItems.append(burger)
    order.selectedItems.append(soda)

    assert order.calculateTotal() == 15.00


# Test 2: Empty order total
# An order with no selected items should have a total of 0.
def test_order_total_is_zero_when_empty():
    order = Order()

    assert order.calculateTotal() == 0.0


# Test 3: Filter menu items by category
# Filtering a menu by "Drinks" should return only the drink items
# and none of the entrees or desserts.
def test_filter_by_category_returns_only_matching_items():
    burger = MenuItem("Spicy Burger", 10.00, "Entrees", 5)
    soda = MenuItem("Large Soda", 5.00, "Drinks", 3)
    tea = MenuItem("Iced Tea", 3.50, "Drinks", 4)
    brownie = MenuItem("Brownie", 4.00, "Desserts", 2)

    menu = Menu()
    menu.items.extend([burger, soda, tea, brownie])

    drinks = menu.filterByCategory("Drinks")

    assert drinks == [soda, tea]


# Test 4: Sort menu items by popularity
# Sorting should return items from highest to lowest popularity rating.
def test_sort_by_popularity_orders_highest_first():
    burger = MenuItem("Spicy Burger", 10.00, "Entrees", 5)
    soda = MenuItem("Large Soda", 5.00, "Drinks", 3)
    brownie = MenuItem("Brownie", 4.00, "Desserts", 2)

    menu = Menu()
    menu.items.extend([brownie, burger, soda])

    sortedItems = menu.sortByPopularity()

    assert sortedItems == [burger, soda, brownie]