# Author: Ho Gia Bao Le
# GitHub username: baole-schools
# Date: 08/11/2025
# Main Program: Product Wishlist

import time
import zmq
import json

def main_menu():
    data = [
        {"name": "Jacket", "price": "99.99", "url": "example.com/jacket", "currency": "USD",},
        {"name": "Flashlight", "price": "9.99", "url": "example.com/flashlight", "currency": "USD",},
        {"name": "Laptop", "price": "999.99", "url": "example.com/laptop", "currency": "USD", },
        {"name": "PS5", "price": "999.99", "url": "example.com/ps5", "currency": "USD", },
    ]

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
        print("[4] - Currency Conversion - Convert a product price to another currency.")
        print("[5] - Summarize the Wishlist - Provide a summary of products in your current wishlist.")
        print("[6] - Update a Product - Update the price of a product.")
        print("[7] - Export the Wishlist - Export your current wishlist as a JSON file.")
        print("[0] - Exit - You can come back any time!\n")
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
                convert_product(data)
                break
            elif option == "5":
                summarize_products(data)
                break
            elif option == "6":
                update_product(data)
                break
            elif option == "7":
                export_products(data)
                break
            elif option == "0":
                print("Thank you for using my software. Good bye!")
                return
            else:
                print(" <!> Invalid option. Please try again. <!> ")
                print("")
                continue

def view_products(data):

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
            name = input("Step 1 of 3: Enter name: ").strip()
            if name:
                break
            print(" <!> Product name cannot be empty! Please try again! <!> ")

        while True:
            print("")
            price = input("Step 2 of 3: Enter price: ").strip()
            try:
                float(price)
                if float(price) <= 0:
                    print(" <!> Invalid price! Please try again! <!> ")
                    continue
                break
            except ValueError:
                print(" <!> Invalid price! Please try again! <!> ")
        price = str(round(float(price), 2))

        # Eliminates currency, always "USD"
        """while True:
            print("")
            currency = input("Step 3 of 4: Enter currency (USD / EUR / GBP): ").strip().upper()
            if currency in ("USD", "EUR", "GBP"):
                break
            print(" <!> Invalid currency! Please try again! <!> ")"""
        currency = "USD"

        while True:
            print("")
            url = input("Step 3 of 3: Enter URL: ").strip()
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

def convert_product(data):
    while True:
        time.sleep(0.1)
        print("")
        print("================================================================================")
        print("CURRENCY CONVERSION")
        print("================================================================================")
        print("")
        print("View a product price in a different currency!")
        print("")
        print("--------------------------------------------------------------------------------")
        print("")
        if not data:
            print("Your current list is empty!")
        else:
            print("Here’s your current products:")
            count = 1
            for product in data:
                name, price, currency = product.get("name"), product.get("price"), product.get("currency")
                print(f"[{count}] - {name} - {price} ({currency})")
                count += 1

            while True:
                print("")
                choice_prod = input("Enter the number for the product you want to convert: ")
                if choice_prod.isdigit() and 0 < int(choice_prod) <= len(data):
                    break
                print(" <!> Invalid product choice! Please try again! <!> ")

            while True:
                print("")
                target = input("Enter the target currency (GBP or EUR): ").strip().upper()
                if target in ("EUR", "GBP"):
                    break
                print(" <!> Invalid currency! Please try again! <!> ")

            context = zmq.Context()
            socket = context.socket(zmq.REQ)
            socket.connect("tcp://localhost:5555")

            index = int(choice_prod) - 1
            product = data[index]
            name, price, currency = product.get("name"), product.get("price"), product.get("currency")
            msg = {
                "name": name,
                "price": price,
                "currency": currency,
                "target": target
            }
            try:
                socket.send_string(json.dumps(msg))
                response = socket.recv_string()
                response = json.loads(response)
                if "error" in response:
                    print(f" <!> Error during conversion! <!>")
                    continue

                print("")
                print(f"The converted price of {response['name']} is {response['price']} ({response["currency"]})")
            except Exception as e:
                print(f" <!> Error during conversion: {e} <!> ")
            finally:
                socket.close()
                context.term()

        print("")
        print("--------------------------------------------------------------------------------")
        print("")
        print("Commands for the software:")
        print("[1] - Convert another product.")
        print("[2] - Return to Main Menu.")
        print("(or enter anything to return)")
        option = input("Enter a number to choose an option: ").strip()
        if option == "1":
            continue
        else:
            return

def summarize_products(data):
    print("")
    print("================================================================================")
    print("SUMMARIZE THE WISHLIST")
    print("================================================================================")
    print("")
    print("View a summary and analysis of all products currently in your wishlist!")
    print("")
    print("--------------------------------------------------------------------------------")
    print("")
    if not data:
        print("Your current list is empty!")
    else:
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:6666")

        try:
            socket.send_string(json.dumps(data))
            response = socket.recv_string()
            response = json.loads(response)
            if "error" in response:
                print(f" <!> Error during summarizing! <!>")
            else:
                print(f"- There are [{response['count']}] products currently in your wishlist for a total [{response['total']} USD].")
                print(f"- The most  expensive product(s): [{', '.join(response['max_product'])}], costing [{response['max_price']} USD].")
                print(f"- The least expensive product(s): [{', '.join(response['min_product'])}], costing [{response['min_price']} USD].")

        except Exception as e:
            print(f" <!> Error during calculation: {e} <!> ")
        finally:
            socket.close()
            context.term()

    print("")
    print("--------------------------------------------------------------------------------")
    print("")
    print("Commands for the software:")
    print("[1] - Return to Main Menu.")
    print("(or enter anything to return)")
    input("Enter a number to choose an option: ")
    return

def update_product(data):
    while True:
        time.sleep(0.1)
        print("")
        print("================================================================================")
        print("UPDATE A PRODUCT")
        print("================================================================================")
        print("")
        print("Update the price of a product and store the price history.")
        print("")
        print("--------------------------------------------------------------------------------")
        print("")
        if not data:
            print("Your current list is empty!")
        else:
            print("Here’s your current products:")
            count = 1
            for product in data:
                name, price, currency = product.get("name"), product.get("price"), product.get("currency")
                print(f"[{count}] - {name} - {price} ({currency})")
                count += 1

            while True:
                print("")
                choice_prod = input("Enter the number for the product you want to update: ")
                if choice_prod.isdigit() and 0 < int(choice_prod) <= len(data):
                    break
                print(" <!> Invalid product choice! Please try again! <!> ")

            while True:
                print("")
                updated = input("Please enter the new price: ").strip()
                try:
                    float(updated)
                    if float(updated) <= 0:
                        print(" <!> Invalid price! Please try again! <!> ")
                        continue
                    break
                except ValueError:
                    print(" <!> Invalid price! Please try again! <!> ")

            updated = str(round(float(updated), 2))

            index = int(choice_prod) - 1
            product = data[index]
            name, price = product.get("name"), product.get("price")
            msg = {
                "name": name,
                "price": price,
                "updated": updated,
            }
            context = zmq.Context()
            socket = context.socket(zmq.REQ)
            socket.connect("tcp://localhost:7777")
            try:
                socket.send_string(json.dumps(msg))
                response = socket.recv_string()
                response = json.loads(response)
                if "error" in response:
                    print(f" <!> Error during updating! <!>")
                    continue
                else:
                    print("")
                    print(f"The price for {name} has been updated successfully!")
                    data[index]["price"] = updated
                    print(f"The price history (from old to new): {response['price']}")

            except Exception as e:
                print(f" <!> Error during conversion: {e} <!> ")
            finally:
                socket.close()
                context.term()

        print("")
        print("--------------------------------------------------------------------------------")
        print("")
        print("Commands for the software:")
        print("[1] - Update another product.")
        print("[2] - Return to Main Menu.")
        print("(or enter anything to return)")
        option = input("Enter a number to choose an option: ").strip()
        if option == "1":
            continue
        else:
            return

def export_products(data):
    print("")
    print("================================================================================")
    print("EXPORT THE WISHLIST")
    print("================================================================================")
    print("")
    print("Save and export your current wishlist a JSON file to store.")
    print("")
    print("--------------------------------------------------------------------------------")
    print("")
    if not data:
        print("Your current list is empty!")
    else:
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:8888")

        try:
            socket.send_string(json.dumps(data))
            response = socket.recv_string()
            response = json.loads(response)
            if "error" in response:
                print(f" <!> Error during exporting! <!>")
            else:
                print(f"Your wishlist has been exported successfully!")
                print(f"The file is stored at: \n"
                      f"{response['path']}")

        except Exception as e:
            print(f" <!> Error during calculation: {e} <!> ")
        finally:
            socket.close()
            context.term()

    print("")
    print("--------------------------------------------------------------------------------")
    print("")
    print("Commands for the software:")
    print("[1] - Return to Main Menu.")
    print("(or enter anything to return)")
    input("Enter a number to choose an option: ")
    return

if __name__ == '__main__':
    main_menu()