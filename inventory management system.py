#  Inventory Management System
inventory = [["Apple", 50, 30, 100],["Banana", 10, 5, 200],["Mango", 80, 60, 50],["Orange", 40, 25, 120],["Grapes", 60, 40, 75]]

users = []   # store user carts
cart = []

while True:
    print("*<<<<<< INVENTORY MANAGEMENT SYSTEM >>>>>>*")
    print("Select Role:")
    print("1. OWNER")
    print("2. USER")
    print("3. EXIT")
    role = input("Enter choice: ")

    if role == "1":   # OWNER
        while True:
            print("**** OWNER MENU ****")
            print("1. Add Item")
            print("2. Remove Item")
            print("3. Update Item")
            print("4. View Inventory")
            print("5. View Users Details")
            print("6. View Report Revenue & Profit")
            print("7. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                name = input("Enter item name: ")
                sp = int(input("Enter selling price: "))
                cp = int(input("Enter cost price: "))
                qty = int(input("Enter quantity: "))
                inventory.append([name, sp, cp, qty])
                print(name, " Item added successfully.")

            elif choice == "2":
                name = input("Enter item name to remove: ")
                found = False
                for item in inventory:
                    if item[0].lower() == name.lower():
                        inventory.remove(item)
                        print(name, " item removed successfully.")
                        found = True
                        break
                if not found:
                    print("Item not found.")

            elif choice == "3":
                name = input("Enter item name to update: ")
                for item in inventory:
                    if item[0].lower() == name.lower():
                        item[1] = int(input("Enter new selling price: "))
                        item[2] = int(input("Enter new cost price: "))
                        item[3] = int(input("Enter new quantity: "))
                        print(name, "updated successfully.")
                        break
                else:
                    print("Item not found.")

            elif choice == "4":
                print("**** INVENTORY ****")
                for item in inventory:
                    print(item[0], "- SP:", item[1], ", CP:", item[2], ", Qty:", item[3])

            elif choice == "5":
                print("**** USERS DETAILS ****")
                for u in users:
                    print("User:", u[0], "Cart:", u[1])

            elif choice == "6":
                print("**** REPORT ****")
                total_revenue = 0
                total_profit = 0
                for item in inventory:
                    revenue = item[1] * item[3]   # SP × Qty
                    profit = (item[1] - item[2]) * item[3]  # (SP - CP) × Qty
                    total_revenue += revenue
                    total_profit += profit
                print("Total Revenue (stock value):", total_revenue)
                print("Total Profit (stock value):", total_profit)

            elif choice == "7":
                break
            else:
                print("Invalid choice.")

    elif role == "2":   # USER
        username = input("Enter your username: ")
        phone = input("Enter 10 digit phone number:")
        if len(phone)==10 and phone.isnumeric():
            print("phone number is valid")
        else:
            print("Invalid phone number!.please enter valid number")
            continue
        cart = []
        while True:
            print("*<<<<<< USER MENU >>>>>>*")
            print("1. Add to Cart")
            print("2. Remove from Cart")
            print("3. Modify Cart")
            print("4. View Cart")
            print("5. Billing")
            print("6. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                print("**** INVENTORY ****")
                for item in inventory:
                    print(item[0], "- SP:", item[1], ", Qty:", item[3])
                name = input("Enter item name: ")
                qty = int(input("Enter quantity: "))
                for item in inventory:
                    if item[0].lower() == name.lower():
                        if qty <= item[3]:
                            cart.append([item[0], item[1], qty])
                            print(qty, name, "added to cart.")
                        else:
                            print("Not enough stock.")
                        break
                else:
                    print("Item not found.")

            elif choice == "2":
                name = input("Enter item to remove: ")
                for c in cart:
                    if c[0].lower() == name.lower():
                        cart.remove(c)
                        print(name, "removed from cart.")
                        break
                else:
                    print("Item not in cart.")

            elif choice == "3":
                name = input("Enter item to modify: ")
                for c in cart:
                    if c[0].lower() == name.lower():
                        qty = int(input("Enter new quantity: "))
                        c[2] = qty
                        print(name, "quantity updated.")
                        break
                else:
                    print("Item not in cart.")

            elif choice == "4":
                print("**** CART ****")
                for c in cart:
                    print(c[0], "- Price:", c[1], ", Qty:", c[2], ", subtotal:", item_total)

            elif choice == "5": 
                print("\n** BILLING **")
                total = 0
                if not cart:
                     print("Cart is empty. Please add items before billing.")
                else:
                    for c in cart:
                        item_total = c[1] * c[2]   # Price × Qty
                        print(c[0], "- Price:", c[1], ", Qty:", c[2], ", Subtotal:", item_total)
                        total += item_total
                        # reduce inventory stock
                        for item in inventory:
                            if item[0] == c[0]:
                               item[3] -= c[2]
                    print("\nTotal Bill:", total)
                    users.append([username, cart])
                    cart = []
    

            elif choice == "6":
                break
            else:
                print("Invalid choice.")

    elif role == "3":   # EXIT
        print("Exiting system...")
        break
    else:
        print("Invalid role.")
