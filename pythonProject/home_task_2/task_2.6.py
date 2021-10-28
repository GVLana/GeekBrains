
stock_list = []
num = 0
pair = ()

while True:
    answer = input("If you want to add a product enter 'y': ")
    if answer.lower() == "y":
        user_name = input("Enter product name: ")
        user_cost = int(input("Enter product price: "))
        user_quantity = int(input("Enter product quantity: "))
        user_unit = input("Enter a unit: ")
        product = {"name": user_name, "cost": user_cost, "quantity": user_quantity, "unit": user_unit}
        product.update()
        num += 1
        pair = (num, product)
        stock_list.append(pair)
    else:
        break

print(stock_list)

i = 0
j = 0

analysis = {}

for i, j in stock_list:
    analysis.setdefault("name", []).append(j["name"])
    analysis.setdefault("cost", []).append(j["cost"])
    analysis.setdefault("quantity", []).append(j["quantity"])
    analysis.setdefault("unit", set()).add(j["unit"])

print(analysis)











