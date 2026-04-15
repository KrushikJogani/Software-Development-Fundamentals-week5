counter = 1000   # starting id value for items

def add_inventory_item():
    global counter   # using global so id can increase every time

    print("Enter New Item Details:")   # asking user to enter details

    # taking all inputs from user
    item_name = input("Enter the item name: ")   # getting item name
    quantity = int(input("Enter quantity of item: "))   # getting quantity
    price = float(input("Price per item: "))   # getting price

    # creating unique item id and then increasing it
    item_id = counter
    counter += 1   # increase for next item

    # calculating total cost of items
    total_value = quantity * price

    print("Adding Inventory Item:")
    print(f"Item Name: {item_name}")   # showing name
    print(f"Item ID: {item_id}")   # showing id
    print(f"Quantity: {quantity}")   # showing quantity
    print(f"Price per Item: ${price}")   # showing price
    print(f"Total value: ${total_value}")   # showing total

    # sending all values back
    return item_name, item_id, quantity, price, total_value

add_inventory_item()
print("Item Added!")


