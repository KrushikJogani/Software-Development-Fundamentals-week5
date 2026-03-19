# task 3

counter = 1000 

def add_inventory_item():
    global counter  # making global for use in this program
    
    print("Enter New Item Details:")   # to get details about new items
    
    item_name = input("Enater the item Name: ")
    quantity = int(input("Enter quantity of item: "))
    price = float(input("Price per Item: "))
    
    item_id = counter  # create unique Item ID
    counter += 1       # set up the increament for counter
    
    total_value = quantity * price  # calculating total value
    
    print("Adding Inventory Item:")  # display item details
    print(f"Item Name: {item_name}")
    print(f"Item ID: {item_id}")
    print(f"Quantity: {quantity}")
    print(f"Price per Item: ${price:.2f}")
    print(f"Total value: ${total_value:.2f}")
    
    # Return the all details 
    return item_name, item_id, quantity, price, total_value


def update_inventory_item():
    
    # calling function for getting item details
    item_name, item_id, quantity, price, total_value = add_inventory_item()
    
    print("\nUpdate Inventory")  # update section
    
    # asking user for new values
    new_quantity = int(input("Enter new quantity: "))
    new_price = float(input("Enter new price: "))
    
    # updating values
    quantity = new_quantity
    price = new_price
    total_value = quantity * price   # recalculating total value
    
    print("Updated Item Details:")   # displaying updated details
    print(f"Item Name: {item_name}")
    print(f"Item ID: {item_id}")
    print(f"Quantity: {quantity}")
    print(f"Price per Item: ${price:.2f}")
    print(f"Total value: ${total_value:.2f}")
    
    # return updated values
    return item_name, item_id, quantity, price, total_value


# running the program
update_inventory_item()