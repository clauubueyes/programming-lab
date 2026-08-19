## FIND THE MOST EXPENSIVE PRODUCT

### Description 
Create a function called find_most_expensive that receives a list of products.

Each product will have a name and a price.

The function should find and return the name of the most expensive product.

### Example: 
```
products = [
    {"name": "Camiseta", "price": 15},
    {"name": "Pantalón", "price": 30},
    {"name": "Zapatillas", "price": 80},
    {"name": "Gorra", "price": 20}
]

find_most_expensive(products)
``` 
### Rules: 
1. You must create a function called find_most_expensive.
2. You must use a for to browse the products.
3. You should compare prices.
4. You should save the most expensive product found up to that moment.
5. You should return the name, not the price.
6. You can't use max().
7. You cannot sort the list with sort() or sorted().