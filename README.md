# Inventory Management System (Flask API)

## Overview
This project is a Flask-based REST API for managing inventory in a retail store. It allows users to perform CRUD operations and integrates an external API to fetch product details.

## Features
- Full CRUD operations (Create, Read, Update, Delete)
- CLI interface supporting all CRUD operations
- External API integration (OpenFoodFacts)
- Ability to fetch product data and add to inventory via CLI
- Persistent storage using JSON file
- Unit tests covering all CRUD operations

## Setup Instructions

1. Clone the repository:
git clone <your-repo-link>

2. Navigate to project folder:
cd inventory-system

3. Create virtual environment:
python -m venv venv

4. Activate virtual environment:
venv\Scripts\activate

5. Install dependencies:
pip install flask requests

6. Run the application:
python app.py

## API Endpoints

- GET /items → Get all items
- POST /items → Add new item
- PATCH /items/<id> → Update item
- DELETE /items/<id> → Delete item
- GET /fetch/<barcode> → Fetch product from external API

## CLI Usage
Run:
python cli.py

## Testing
Run:
python test_app.py

## Notes
- Data is stored in a local JSON file (`inventory.json`)
- External API may fail due to network issues but is implemented correctly