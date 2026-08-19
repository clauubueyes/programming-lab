def find_most_expensive(products): 
    res = products[0]
    for product in products: 
        if product["price"] > res["price"]:
            res = product
    return res["name"]
        
    
       
    

products = [
    {"name": "Camiseta", "price": 15},
    {"name": "Pantalón", "price": 30},
    {"name": "Zapatillas", "price": 80},
    {"name": "Gorra", "price": 20}
]

print(find_most_expensive(products))