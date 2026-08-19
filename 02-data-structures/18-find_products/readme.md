## FIND PRODUCTS 

### Description 

Create a function find_products thas recives a dictionary where the keys are the products and the values are the prices. 

The function should: 
    - Check if product_name exists in the dictionary.
    - If it exists, return its price.
    - If it does not exist, return None.
### Example
products = {
    "laptop": 900,
    "mouse": 25,
    "keyboard": 60,
    "monitor": 200
}

find_product(products, "mouse") -> 25
find_product(products, "tablet") -> None