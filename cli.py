import requests

BASE_URL = "http://127.0.0.1:5000"

def view_items():
    res = requests.get(f"{BASE_URL}/items")
    print("\nInventory:")
    print(res.json())

def add_item():
    name = input("Name: ")
    quantity = int(input("Quantity: "))

    res = requests.post(f"{BASE_URL}/items", json={
        "name": name,
        "quantity": quantity
    })
    print(res.json())

def update_item():
    index = input("Enter item index to update: ")
    quantity = int(input("New quantity: "))

    res = requests.patch(f"{BASE_URL}/items/{index}", json={
        "quantity": quantity
    })
    print(res.json())

def delete_item():
    index = input("Enter item index to delete: ")

    res = requests.delete(f"{BASE_URL}/items/{index}")
    print(res.json())

# 🔥 NEW: fetch from external API and add
def fetch_and_add():
    barcode = input("Enter barcode: ")

    res = requests.get(f"{BASE_URL}/fetch/{barcode}")
    data = res.json()

    if "error" in data:
        print(data)
        return

    print("Fetched product:", data)

    confirm = input("Add this item to inventory? (y/n): ")

    if confirm.lower() == "y":
        add_res = requests.post(f"{BASE_URL}/items", json=data)
        print(add_res.json())

def menu():
    while True:
        print("\n1. View Items")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Fetch Product (API)")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            view_items()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            fetch_and_add()
        else:
            break

if __name__ == "__main__":
    menu()