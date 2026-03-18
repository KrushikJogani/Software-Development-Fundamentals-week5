counter = 1000 

def add_inventory_item():
    global counter  #making global for use in this program
    
    print("Enter New Item Details:")    #to get get details about new items
    
    item_name = input("Enater the item Name: ")
    quantity = int(input("Enter quantity of item: "))
    price = float(input("Price per Item: "))
    
    item_id = counter # create unique Item ID
    counter += 1 #set up the increament for counter 

    total_value = quantity * price # calculating total value
    
    print("Adding Inventory Item:")
    print(f"Item Name: {item_name}")
    print(f"Item ID: {item_id}")
    print(f"Quantity: {quantity}")
    print(f"Price per Item: ${price}")
    print(f"Total value: ${total_value}")

    # Return the all details 
    return item_name, item_id, quantity, price , total_value

add_inventory_item()
print("Item Added!")


