# Author: Ho Gia Bao Le
# GitHub username: baole-schools
# Date: 07/28/2025
# Description: Main Program - Sprint 1

import time

def main_menu():
    data = [
        {"name": "Jacket", "price": "99.99", "url": "example.com/jacket", "currency": "USD",},
        {"name": "Flashlight", "price": "9.99", "url": "example.com/flashlight", "currency": "EUR",},
        {"name": "Laptop", "price": "999.99", "url": "example.com/laptop", "currency": "GBP", },
    ]
    '''data = []'''

    while True:
        time.sleep(0.1)
        print("")
        print("================================================================================")
        print("WELCOME TO THE SHOPPING WISHLIST")
        print("================================================================================")
        print("")
        print("This software helps you track the price of your favorite products!")
        print("")
        print("--------------------------------------------------------------------------------")
        print("")
        print("Commands for the software:")
        print("[1] - View all Products - See all products and their current prices.")
        print("[2] - Add a Product - Save a new product to your wishlist.")
        print("[3] - Delete a Product - Remove a product you no longer desire.")
        print("[4] - Exit - You can come back any time!\n")
        while True:
            option = input("Enter a number to choose an option: ").strip()
            if option == "1":
                view_products(data)
                break
            elif option == "2":
                add_product(data)
                break
            elif option == "3":
                del_product(data)
                break
            elif option == "4":
                print("Thank you for using my software. Good bye!")
                return
            else:
                print(" <!> Invalid option. Please try again. <!> ")
                print("")
                continue

def view_products(data):
    while True:
        time.sleep(0.1)
        print("")
        print("================================================================================")
        print("VIEW ALL PRODUCTS")
        print("================================================================================")
        print("")
        print("View all products currently on your wishlist!")
        print("")
        print("--------------------------------------------------------------------------------")
        print("")
        if not data:
            print("Your current list is empty!")
        else:
            for product in data:
                name, price, url, currency = product.get("name"), product.get("price"), product.get("url"), product.get("currency")
                print(f"{name} - {price} ({currency}) - {url}")

        print("")
        print("--------------------------------------------------------------------------------")
        print("")
        print("Commands for the software:")
        print("[1] - Return to Main Menu.")
        print("(or enter anything to return)")
        input("Enter a number to choose an option: ")
        return

def add_product(data):
    while True:
        time.sleep(0.1)
        print("")
        print("================================================================================")
        print("ADD A PRODUCT")
        print("================================================================================")
        print("")
        print("Add a new product to your wishlist!")
        print("Provide the product details so we can save it for you!")
        print("TIPS: You can add and save any product.")
        print("TIPS: If you added a product incorrectly, you can delete it and add a correct one.")
        print("")
        print("--------------------------------------------------------------------------------")
        print("")
        print("Save the product with a simple process:")
        while True:
            print("")
            name = input("Step 1 of 4: Enter name: ").strip()
            if name:
                break
            print(" <!> Product name cannot be empty! Please try again! <!> ")

        while True:
            print("")
            price = input("Step 2 of 4: Enter price: ").strip()
            try:
                float(price)
                if float(price) <= 0:
                    print(" <!> Invalid price! Please try again! <!> ")
                    continue
                break
            except ValueError:
                print(" <!> Invalid price! Please try again! <!> ")

        while True:
            print("")
            currency = input("Step 3 of 4: Enter currency (USD / EUR / GBP): ").strip().upper()
            if currency in ("USD", "EUR", "GBP"):
                break
            print(" <!> Invalid currency! Please try again! <!> ")

        while True:
            print("")
            url = input("Step 4 of 4: Enter URL: ").strip()
            if url:
                break
            print(" <!> Product URL cannot be empty! Please try again! <!> ")

        data.append({
            "name": name,
            "price": price,
            "url": url,
            "currency": currency
        })
        print("")
        print("The product has been added successfully!")
        print(f"{name} - {price} ({currency}) - {url}")
        print("")
        print("--------------------------------------------------------------------------------")
        print("")
        print("Commands for the software:")
        print("[1] - Add another product.")
        print("[2] - Return to Main Menu.")
        print("(or enter anything to return)")
        option = input("Enter a number to choose an option: ").strip()
        if option == "1":
            continue
        else:
            return

def del_product(data):
    while True:
        time.sleep(0.1)
        print("")
        print("================================================================================")
        print("DELETE A PRODUCT")
        print("================================================================================")
        print("")
        print("Delete an unwanted or incorrect product!")
        print("TIPS: You can always add a deleted product back to your wishlist.")
        print("")
        print("--------------------------------------------------------------------------------")
        print("")
        if not data:
            print("Your current list is empty!")
        else:
            print("Here’s your current products:")
            count = 1
            for product in data:
                name, url = product.get("name"), product.get("url")
                print(f"[{count}] - {name} - {url}")
                count += 1
            print("[ALL] - ALL - Delete all products.")
            print("")
            while True:
                choice_prod = input("Enter the number for the product you want to delete,\n"
                               "Or type ALL (all uppercases) to delete all products: ").strip()
                if choice_prod == "ALL":
                    print("")
                    print(f"Are you sure you want to delete 'ALL'?")
                    print(" <!><!><!> Remove ALL current data <!><!><!> ")
                    print("")
                    print("[1] - Yes.")
                    print("[2] - No - Back to Main Menu.")
                    print("(or enter anything to return)")
                    print("")
                    choice_clear = input("Enter a number to choose an option: ").strip()
                    if choice_clear == "1":
                        data.clear()
                        print("")
                        print("All products have been deleted successfully!")
                        break
                    else:
                        return
                elif choice_prod.isdigit() and 0 < int(choice_prod) <= len(data):
                    index = int(choice_prod) - 1
                    print("")
                    print(f"Are you sure you want to delete '{data[index]["name"]}'?")
                    print(" <!><!><!> Also remove associated data <!><!><!> ")
                    print("")
                    print("[1] - Yes.")
                    print("[2] - No - Back to Main Menu.")
                    print("(or enter anything to return)")
                    print("")
                    choice_del = input("Enter a number to choose an option: ").strip()
                    if choice_del == "1":
                        data.pop(index)
                        print("")
                        print("The product been deleted successfully!")
                        break
                    else:
                        return
                else:
                    print(" <!> Invalid option. Please try again. <!> ")
                    print("")
        print("")
        print("--------------------------------------------------------------------------------")
        print("")
        print("Commands for the software:")
        print("[1] - Delete another product.")
        print("[2] - Return to Main Menu.")
        print("(or enter anything to return)")
        option = input("Enter a number to choose an option: ").strip()
        if option == "1":
            continue
        else:
            return

if __name__ == '__main__':
    main_menu()