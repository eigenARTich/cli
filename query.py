import data


def print_menu():
    print("1. List items by warehouse")
    print("2. Search an item and place an order")
    print("3. Quit")


def list_items_by_warehouse():
    print("Items in Warehouse 1:")
    for item in data.warehouse1:
        print("- " + item)
    print("Items in Warehouse 2:")
    for item in data.warehouse2:
        print("- " + item)


def search_and_order_item():
    item_name = input("What item are you looking for? ")
    total_amount = 0
    warehouse1_has_item = False
    warehouse2_has_item = False
    for item in data.warehouse1:
        if item == item_name:
            total_amount += 1
            warehouse1_has_item = True
    for item in data.warehouse2:
        if item == item_name:
            total_amount += 1
            warehouse2_has_item = True
    if total_amount > 0:
        print("Total amount of " + item_name + " in stock: " + str(total_amount))
        if warehouse1_has_item and warehouse2_has_item:
            print("Item is available in both warehouses.")
            if data.warehouse1.count(item_name) > data.warehouse2.count(item_name):
                print("Warehouse 1 has the most amount of " + item_name + " with a total of " + str(
                    data.warehouse1.count(item_name)))
            elif data.warehouse2.count(item_name) > data.warehouse1.count(item_name):
                print("Warehouse 2 has the most amount of " + item_name + " with a total of " + str(
                    data.warehouse2.count(item_name)))
            else:
                print("Both warehouses have the same amount of " + item_name + ".")
        elif warehouse1_has_item:
            print("Item can be found in Warehouse 1.")
        elif warehouse2_has_item:
            print("Item can be found in Warehouse 2.")
    else:
        print("Item not in stock.")
    place_order = input("Do you want to place an order for " + item_name + "? (y/n) ")
    if place_order == "y":
        desired_amount = int(input("How many do you want? "))
        if desired_amount <= total_amount:
            print("Order placed for " + str(desired_amount) + " " + item_name + ".")
        else:
            order_max = input(
                "Desired amount is higher than the total available. Do you want to order the maximum available instead? (y/n) ")
            if order_max == "y":
                print("Order placed for " + str(total_amount) + " " + item_name + ".")
            else:
                print("No order placed.")
    else:
        print("No order placed.")


def main():
    name = input("What's your name? ")
    print("Hello " + name + "!")
    print_menu()
    choice = input("Pick a choice (1-3): ")
    while choice != "3":
        if choice == "1":
            list_items_by_warehouse()
            break
        elif choice == "2":
            search_and_order_item()
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            choice = input("Pick a choice (1-3): ")
    print("Thank you for visiting, " + name + "!")


if __name__ == '__main__':
    main()
