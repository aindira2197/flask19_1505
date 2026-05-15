warehouse = {
    "olma": 12,
    "banan": 5,
    "uzum": 20
}

for product, amount in warehouse.items():
    print(product, amount)

product_name = input("Mahsulot nomi: ")

if product_name in warehouse:
    warehouse[product_name] += 10
else:
    warehouse[product_name] = 10

print("Yangilangan ombor:")

for product, amount in warehouse.items():
    print(product, amount)
