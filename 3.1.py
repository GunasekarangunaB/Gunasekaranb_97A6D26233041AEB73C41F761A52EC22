
def linear_search_product(products, target):
    indices = []
    for i in range(len(products)):
        if products[i] == target:
            indices.append(i)
    return indices


products = ["apple", "banana", "orange", "banana", "grape"]
target_product = "banana"

indices = linear_search_product(products, target_product)
if len(indices) > 0:
    print("The product", target_product, "was found at the following indices:", indices)
else:
    print("The product", target_product, "was not found.")