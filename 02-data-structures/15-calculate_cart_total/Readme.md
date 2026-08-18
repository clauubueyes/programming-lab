## SHIPPING CART

### Definition 
Create a function called calculate_cart_total(cart) that receives a list of items in a shopping cart. Each item is a dictionary with the keys "name", "price" and "quantity". The function should return the total accumulated price of the cart.

### Example 
cart = [
    {"name": "Camiseta", "price": 15.0, "quantity": 2},
    {"name": "Pantalón", "price": 30.0, "quantity": 1},
    {"name": "Calcetines", "price": 5.0, "quantity": 3}
]

calculate_cart_total(cart) -> 75.00

### Rules 
1. If the cart is empty (cart = []), it should return 0.0.
2. Remember to multiply the price by the quantity in each product before adding it to the total.