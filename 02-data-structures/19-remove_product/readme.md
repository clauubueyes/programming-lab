##  REMOVE PRODUCT 

### Description 
create a function remove_product() that recives a dictionary of products and the name of the product 
The function must:
- Check if product_name exists in products.
- If it exists, remove it from the dictionary.
- Return the updated dictionary.

If it does not exist, return the dictionary unchanged.
### Example 
products = {
    "laptop": 900,
    "mouse": 25,
    "keyboard": 60,
    "monitor": 200
}
remove_product(products, "mouse")  

### Result 

{
    "laptop": 900,
    "keyboard": 60,
    "monitor": 200
}