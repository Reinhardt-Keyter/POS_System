# Define a list to store products (each product is a dictionary)
products = []

# Function to add a product to the list
def add_product():
    print("Enter product name:")
    product_name = input()

    print("Enter product price:")
    product_price = float(input())  # Convert input to float

    products.append({"name": product_name, "price": product_price})

    print(f"Product '{product_name}' added successfully.")


# Function to remove a product from the list
def remove_product():
    print("Enter product name to remove:")
    product_name = input()

    found = False
    for product in products:
        if product["name"].lower() == product_name.lower():
            products.remove(product)
            print(f"Product '{product_name}' removed successfully.")
            found = True
            break  # Exit the loop once product is found and removed

    if not found:
        print(f"Product '{product_name}' not found.")


# Function to display all products and calculate total
def display_products_and_total():
    if not products:
        print("No products added yet.")
        return

    print("List of Products:")
    total = 0
    for product in products:
        print(f"{product['name']} R{product['price']:.2f}")
        total += product['price']
    print("---------------")
    print(f"Total R{total:.2f}")


# Main function to drive the POS system
def main():
    while True:
        print("\nSelect an option:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Display Products and Total Amount")
        print("4. Exit")

        option = input()

        if option == '1':
            add_product()
        elif option == '2':
            remove_product()
        elif option == '3':
            display_products_and_total()
        elif option == '4':
            print("Exiting, Goodbye!.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
