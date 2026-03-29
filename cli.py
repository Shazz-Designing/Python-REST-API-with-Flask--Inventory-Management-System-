import requests

BASE_URL = "http://127.0.0.1:5000"

def view_items():
    res = requests.get(f"{BASE_URL}/items")
    print("\nInventory:")
    print(res.json())

def add_item():
    name = input("Name: ")
    quantity = input("Quantity: ")

    res = requests.post(f"{BASE_URL}/items", json={
        "name": name,
        "quantity": int(quantity)
    })
    print(res.json())

def menu():
    while True:
        print("\n1. View Items\n2. Add Item\n3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            view_items()
        elif choice == "2":
            add_item()
        else:
            break

if __name__ == "__main__":
    menu()