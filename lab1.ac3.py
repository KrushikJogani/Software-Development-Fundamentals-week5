# Task 4: Inventory Management

counter = 1000 

def add_inventory_item():
    global counter  # making global for use in this program
    
    print("Enter New Item Details:")  # to get details about new items
    
    item_name = input("Enter the item Name: ")
    quantity = int(input("Enter quantity of item: "))
    price = float(input("Price per Item: "))
    
    item_id = counter  # create unique Item ID
    counter += 1       # set up the increament for counter
    
    total_value = quantity * price  # calculating total value
    
    # display item details
    print("Adding Inventory Item:")
    print(f"Item Name: {item_name}")
    print(f"Item ID: {item_id}")
    print(f"Quantity: {quantity}")
    print(f"Price per Item: ${price:.2f}")
    print(f"Total Value: ${total_value:.2f}")
    
    # Return the all details 
    return item_name, item_id, quantity, price, total_value

def update_inventory_item():
    item_name, item_id, quantity, price, total_value = add_inventory_item()
    
    print("Update Inventory")
    
    new_quantity = int(input("Enter new quantity: "))
    new_price = float(input("Enter new price: "))
    
    quantity = new_quantity
    price = new_price
    total_value = quantity * price  # Recalculate total value
    
    return item_name, item_id, quantity, price, total_value


def display_item(item_name, item_id, quantity, price, total_value):
    print("Displaying Inventory Item:")  # Heading
    
    print(f"Item Name: {item_name}")
    print(f"Item ID: {item_id}")
    print(f"Quantity: {quantity}")
    print(f"Price per Item: ${price}")
    print(f"Total Value: ${total_value}")
    
    return item_name, item_id, quantity, price, total_value


item_name, item_id, quantity, price, total_value = add_inventory_item()

# Display the added item
display_item(item_name, item_id, quantity, price, total_value)

# Update the item
item_name, item_id, quantity, price, total_value = update_inventory_item()

# Display updated item
display_item(item_name, item_id, quantity, price, total_value)
