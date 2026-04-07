from flask import Flask, jsonify, request
import json
import os
import requests

app = Flask(__name__)

DATA_FILE = "inventory.json"

# Load data
def load_inventory():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Save data
def save_inventory(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

inventory = load_inventory()

@app.route('/')
def home():
    return "Inventory API is running!"

# GET all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(inventory)

# POST add item
@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    inventory.append(data)
    save_inventory(inventory)
    return jsonify({
        "message": "Item added",
        "item": data
    })

# PATCH update item
@app.route('/items/<int:index>', methods=['PATCH'])
def update_item(index):
    if index < len(inventory):
        data = request.get_json()
        inventory[index].update(data)
        save_inventory(inventory)
        return jsonify({
            "message": "Item updated",
            "item": inventory[index]
        })
    return jsonify({"error": "Item not found"})

# DELETE item
@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    if index < len(inventory):
        removed = inventory.pop(index)
        save_inventory(inventory)
        return jsonify({
            "message": "Item deleted",
            "item": removed
        })
    return jsonify({"error": "Item not found"})

# 🌍 IMPROVED EXTERNAL API
@app.route('/fetch/<barcode>', methods=['GET'])
def fetch_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return jsonify({"error": "API request failed"})

        try:
            data = response.json()
        except:
            return jsonify({"error": "Invalid response from API"})

        if data.get("status") == 1:
            product = data["product"]

            # 👇 CLEAN DATA (this is the upgrade)
            return jsonify({
                "name": product.get("product_name") or "Unknown",
                "brand": product.get("brands") or "Unknown",
                "category": product.get("categories") or "General",
                "barcode": barcode
            })

        return jsonify({"error": "Product not found"})

    except Exception as e:
        return jsonify({
            "error": "Something went wrong",
            "details": str(e)
        })

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)