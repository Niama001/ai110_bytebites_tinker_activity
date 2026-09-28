# ByteBites

Backend logic for ByteBites, a campus food ordering app, built with Python classes and simple algorithms. This project was built for the CodePath AI110 "Tinker: ByteBites" activity using an AI-assisted workflow: design a UML diagram, implement the classes, add algorithms, and verify everything with tests.

## Classes

| Class | Purpose |
|-------|---------|
| `Customer` | Stores a customer's name and purchase history |
| `MenuItem` | Stores an item's name, price, category, and popularity rating |
| `Menu` | Holds all menu items, with filtering and sorting |
| `Order` | Stores selected items and calculates the total cost |

## Features

- **Filter by category:** `Menu.filterByCategory("Drinks")` returns only items in that category.
- **Sort by popularity:** `Menu.sortByPopularity()` returns items from highest to lowest rating.
- **Order totals:** `Order.calculateTotal()` adds up the selected items' prices (an empty order returns `0.0`).

## Project Structure

```
bytebites_tinker_activity/
├── models.py                  # Customer, MenuItem, Menu, Order
├── test_bytebites.py          # pytest test suite
├── bytebites_spec.md          # client feature request and candidate classes
├── ByteBites_Design_Reference.md  # behavioral instructions for the AI assistant
├── bytebites_design.mmd       # final Mermaid class diagram
└── draft_from_copilot.mmd     # first draft diagram (before the reference file)
```

## Getting Started

Requires Python 3.

Run the manual demo scenario:

```
python models.py
```

Run the tests:

```
pip install pytest
python -m pytest
```

## Example

```python
from models import MenuItem, Menu, Order

burger = MenuItem("Spicy Burger", 10.00, "Entrees", 5)
soda = MenuItem("Large Soda", 5.00, "Drinks", 3)

menu = Menu()
menu.items.extend([burger, soda])

order = Order()
order.selectedItems.extend([burger, soda])

print(order.calculateTotal())  # 15.0
```