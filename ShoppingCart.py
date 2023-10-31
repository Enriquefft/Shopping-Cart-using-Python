"""A simple shopping cart program."""

from typing import Final, Optional

done = False
DEFAULT_STORE_SIZE: Final[int] = 10


class ShoppingCart:
    """Represents a shopping cart."""

    def __init__(self):
        """Create a new, empty shopping cart."""
        self.items = []

    def addToCart(self, item):
        """Add an item to the cart."""
        self.items.append(item)

    def removeFromCart(self, itemindex):
        """Remove an item from the cart."""
        self.items.pop(itemindex)

    def priceCart(self):
        """Return the price of all items in the cart."""
        price = 0
        for x in self.items:
            price = price + x.price
        return price

    def listCart(self):
        """List all items in the cart."""
        cid = 0
        print("Cart Items:")
        for x in self.items:
            print(x.name, x.price, cid)
            cid = cid + 1
        print("")


class Item:
    """Represents a store item."""

    def __init__(self, price, name):
        """Create a new item."""
        self.price = price
        self.name = name


itemNames: Final[list[str]] = [
    "HDMI Cable",
    "Keyboard",
    "Headphones",
    "RAM",
    "Phone",
    "Monitor",
    "Mouse",
    "CPU",
    "GPU",
    "Motherboard",
    "SSD",
    "HDD",
    "Power Supply",
    "Ethernet Cable",
    "USB Cable",
]


class Store:
    """Represents a store."""

    def __init__(self, storefile: Optional[str] = None):
        """Create a new store."""
        self.items: list[Item] = []

        if storefile is None:
            for i in range(DEFAULT_STORE_SIZE):
                self.items.append(Item(i, itemNames[i]))

    def listStore(self):
        """List all items in the store."""
        item_n = 0
        for x in self.items:
            # Format print name{10} price{3} item_n{2}
            print(f"{x.name:10} {x.price:3} {item_n:2}")
            item_n += 1
        print("")

    def __getitem__(self, index: int) -> Item:
        """Get an item from the store."""
        return self.items[index]


def printInstructions():
    """Print the instructions for the user."""
    print("Type C to view your cart items")
    print("Type R to item from your cart")
    print("Type an item number to buy it")
    print("Type P to get the total cart price")
    print("Type X to exit")


def removeItem(cart: ShoppingCart) -> None:
    """Recieve input and remove an item from the cart."""
    input1 = input("Type a cart object ID to remove")
    cart.removeFromCart(input1)


def handleInput(store: Store, in_var: str, cart: ShoppingCart) -> None:
    """Handle the input from the user."""
    char_inputs = ["C", "R", "P", "X"]
    if (in_var == "C"):
        cart.listCart()
    if (in_var == "R"):
        removeItem(cart)
    if (in_var == "P"):
        print("The items in your cart currently cost")
        print(cart.priceCart())
    if (in_var == "X"):
        global done
        done = True
    if in_var not in char_inputs:
        try:
            cart.addToCart(store[int(in_var)])
        except ValueError:
            print("you have entered an illegal character!")


store = Store()
cart = ShoppingCart()

while not done:
    store.listStore()
    printInstructions()
    input_var = input("choose an item to buy(type the id)")
    handleInput(store, input_var, cart)
