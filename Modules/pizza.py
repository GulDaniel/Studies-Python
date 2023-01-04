def make_pizza(size, *toppings):
    """Show the pizza that we'll make."""
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
