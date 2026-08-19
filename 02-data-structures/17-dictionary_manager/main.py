

def update_product(product, property, price):
    product[property] = price
    return product

product = {
    "name": "Camiseta",
    "price": 15,
    "stock": 10
}

print(update_product(product, "price", 20))