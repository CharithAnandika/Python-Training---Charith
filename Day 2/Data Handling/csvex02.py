import csv

csv_file_name = "product.csv"
target_value = "True"  # ex : filter availability == "True"
filtered_stock = []

try:
    with open(csv_file_name,mode='r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row.get('availability') == target_value:
                filtered_stock.append(row)

    print(f"filtered stock : {filtered_stock}")
except IOError as e:
    print(f"Error reading {csv_file_name}: {e}")
