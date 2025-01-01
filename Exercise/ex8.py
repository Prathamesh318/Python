class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price
        print(f"Added {item} with price {price}.")

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
            print(f"Removed {item}.")
        else:
            print(f"{item} not found in the cart.")

    def calculate_total(self):
        total = sum(self.items.values())
        print(f"Total price: {total}")
        return total


cart = ShoppingCart()
cart.add_item("Apple", 10)
cart.add_item("Banana", 5)
cart.remove_item("Apple")
cart.calculate_total()
