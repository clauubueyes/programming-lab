def find_product(products, product_name): 
    if product_name in products: 
        return products[product_name]

products = {
    "laptop": 900,
    "mouse": 25,
    "keyboard": 60,
    "monitor": 200
}
print(find_product(products, "mouse"))
print(find_product(products, "tablet"))