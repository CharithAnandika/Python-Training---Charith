import csv

inventory = [
    {"id" : "P001", "name" : "laptop", "price" : 1200, "stock" : 50},
    {"id" : "P002", "name" : "mouse", "price" : 25, "stock" : 150},
    {"id" : "P003", "name" : "keyboard", "price" : 75, "stock" : 70},
    {"id" : "P004", "name" : "monitor", "price" : 300, "stock" : 25},
    {"id" : "P005", "name" : "webcam", "price" : 50, "stock" : 15},
]

print("---initial inventory---")

for product in inventory:
    print(f"{product['id']} - {product['name']} ({product['price']}), stock: {product['stock']}")

#def update_stock(product_id, qty):
#    found = False
#    for product in inventory:
#       if product['id'] == product_id:
#           if product['stock'] + qty >= 0:
#                   product['stock'] = product['stock'] + qty
#                   print(f"updated stock for {product['name']} ID : {product['id']}")
#           else:
#                print("error : not enough stocks for {product['name']}")
#                 found = True
#                 break
#    if not found:
#        print(f"error: product with id '{product_id}' not fount in the inventory")


def update_stock(product_id, qty):
    # Track if product was found
    for product in inventory:
        if product['id'] == product_id:
            # Found matching product—check stock
            if product['stock'] + qty >= 0:
                product['stock'] += qty
                print(f"updated stock for {product['name']} ID : {product['id']}")
            else:
                print(f"error: not enough stock for {product['name']}")
            return  # exit early in either case

    # If loop finishes without return, product wasn't found
    print(f"error: product with id '{product_id}' not found in the inventory")

#result = update_stock(P001,100)


def get_low_stock_products(threshold):
      low_stock_products = []
      for product in inventory:
          if product['stock'] <= threshold:
              low_stock_products.append(product['name'])
      return low_stock_products

updated_items = update_stock("P001",-10)


low_items = get_low_stock_products(30)             
print(low_items) 

for product in inventory:
    print(f"{product['id']} - {product['name']} ({product['price']}), stock: {product['stock']}")