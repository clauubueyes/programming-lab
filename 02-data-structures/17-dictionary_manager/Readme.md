## DICTIONARY MANAGER 

### Description 
Create a function called update_product that receives:
 - A dictionary that represents a product.
 - The name of a property.
 - A new value for that property.
The function should update the product with the new value and return the updated dictionary.

### Example 
product = {
    "name": "Camiseta",
    "price": 15,
    "stock": 10
}

update_product(product, "price", 20) 

Result: 
{
    "name": "Camiseta",
    "price": 15,
    "stock": 25
}