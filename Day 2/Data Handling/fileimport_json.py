import json
import datetime

product_data = {
    "product": [
        {"id": "A1", "name": "keyboard", "price": 75.00,  "available": True},
        {"id": "A2", "name": "mouse",    "price": 25.00,  "available": False},
        {"id": "A3", "name": "monitor",  "price": 300.00, "available": True}
    ],
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d")
}
json_file_name = "product.json"

try:
    with open(json_file_name, mode='w', encoding='utf-8') as json_file:
        json.dump(product_data, json_file, indent=10)
    print(f"Successfully wrote to {json_file_name}")
except IOError as e:
    print(f"Error writing to {json_file_name}: {e}")
