"""
Файлы с выгрузками должны называться {{shop_num}}_{{cash_num}}.csv. Здесь {{shop_num}} - номер магазина, а {{cash_num}} - номер кассы. 
В одном магазине может быть много касс - у каждой своя выгрузка. Пример названия: 11_2.csv - 11 магазин, 2 касса.

Формат выгрузки:
doc_id - численно-буквенный идентификатор чека
item - название товара
category - категория товара (бытовая химия, текстиль, посуда и т.д.)
amount - кол-во товара в чеке
price - цена одной позиции без учета скидки
discount - сумма скидки на эту позицию (может быть 0)

Примечание: В одном чеке может быть несколько строк с разными товарами.
"""

import pandas as pd
import numpy as np
import string
import random
import os


def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return "".join(random.choice(letters) for _ in range(length))


items = [
    "bread",
    "butter",
    "milk",
    "chicken",
    "cereals",
    "sugar",
    "pork",
    "tomato",
    "onion",
    "tea",
    "pasta",
    "potato",
    "eggs",
    "oil",
    "fish",
    "skyrim",
]

categories = {
    "bread": "Bakery",
    "butter": "Dairy",
    "milk": "Dairy",
    "chicken": "Meat",
    "cereals": "Cereals",
    "sugar": "Groceries",
    "pork": "Meat",
    "tomato": "Vegetables",
    "onion": "Vegetables",
    "tea": "Beverages",
    "pasta": "Groceries",
    "potato": "Vegetables",
    "eggs": "Dairy",
    "oil": "Groceries",
    "fish": "Seafood",
    "skyrim": "Gaming",
}


def generate_data(shop_num, cash_num, num_rows):
    data = {
        "doc_id": [generate_random_string(10) for _ in range(num_rows)],
        "item": [random.choice(items) for _ in range(num_rows)],
        "amount": np.random.randint(1, 4, num_rows),
        "price": np.random.uniform(50, 300, num_rows),
    }
    data["discount"] = data["price"] * np.random.uniform(0, 0.2, num_rows)
    data["category"] = [categories[item] for item in data["item"]]
    df = pd.DataFrame(data)

    # Ensure directory exists
    os.makedirs("module-8-project/data", exist_ok=True)
    df.to_csv(f"module-8-project/data/{shop_num}_{cash_num}.csv", index=False)


# Example usage
shops = [11, 12, 13]
cashes = [1, 2, 3]

# Randomly choose 1 to 3 shops non-repeatable
num_shops = random.randint(1, 3)
selected_shops = random.sample(shops, num_shops)

for shop in selected_shops:
    # Randomly choose 1 to 3 cashes non-repeatable for each shop
    num_cashes = random.randint(1, 3)
    selected_cashes = random.sample(cashes, num_cashes)

    for cash in selected_cashes:
        generate_data(shop, cash, random.randint(5, 21))
