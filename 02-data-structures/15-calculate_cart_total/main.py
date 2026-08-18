def calculate_cart_total(cart):
    total= 0
    for item in cart: 
        total += item["price"] * item["quantity"]
    return total

cart = [
    {"name": "Camiseta", "price": 15.0, "quantity": 2},
    {"name": "Pantalón", "price": 30.0, "quantity": 1},
    {"name": "Calcetines", "price": 5.0, "quantity": 3}
]
print(calculate_cart_total(cart))