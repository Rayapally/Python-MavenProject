class ShoppingCart:

    def __init__(self):
        """
        Initialize the ShoppingCart class with an empty dictionary to store items.
        """
        self.items = {}

    def add_item(self, item_name: str, quantity: int = 1) -> None:
        """
        Add an item to the shopping cart.

        If the item already exists in the cart, increase the quantity.

        :param item_name: The name of the item to add.
        :param quantity: The quantity of the item to add (default: 1).
        :raises ValueError: If the quantity is not a positive integer.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        if item_name not in self.items:
            self.items[item_name] = quantity
        else:
            self.items[item_name] += quantity

    def remove_item(self, item_name, quantity=1):
        """
        Remove an item from the shopping cart.

        If the item's quantity becomes 0 or less, remove the item from the cart.

        :param item_name: The name of the item to remove.
        :param quantity: The quantity of the item to remove (default: 1).
        :return: None
        """
        if item_name in self.items:
            self.items[item_name] -= quantity
            if self.items[item_name] <= 0:
                del self.items[item_name]
        else:
            print(f"{item_name} is not in the cart.")  # Added print statement

    def get_total(self):
        """
        Calculate the total cost of the items in the shopping cart.

        :return: The total cost of the items in the cart.
        """
        total = 0
        for item, quantity in self.items.items():
            # Assume price lookup logic here (e.g., from a database)
            total += quantity * 10  # Placeholder price
        return total