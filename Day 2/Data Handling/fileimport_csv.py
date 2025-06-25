import csv


product_data = {
    "product": [
        {"id": "A1", "product name": "keyboard", "price": 75.00,  "availability": True},
        {"id": "A2", "product name": "mouse",    "price": 25.00,  "availability": False},
        {"id": "A3", "product name": "monitor",  "price": 300.00, "availability": True}
    ],
    
}
csv_file_name = "product.csv"

fieldnames = ["id", "product name","price", "availability"]

try:
    with open(csv_file_name, mode='w', newline='') as csv_file:
        
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(product_data["product"])

    print(f"Successfully wrote to {csv_file_name}")

except IOError as e:
    print(f"Error writing to {csv_file_name}: {e}")