def remove_product(products, product_name):
    if product_name in products: 
        del products[product_name]
    return products
    
    

products = {
    "laptop": 900,
    "mouse": 25,
    "keyboard": 60,
    "monitor": 200
}

print(remove_product(products, "mouse"))