"""
Напишите скрипт, который генерирует N (кол-во магазинов) выгрузок в формате csv в папку data/. Формат выгрузки будет указан ниже.
Автоматизируйте этот скрипт так, чтобы он работал каждый день, кроме воскресенья. Вы можете это сделать с помощью того инструмента, который вам удобен - cron 
или планировщик Windows (зависит от вашей операционной системы).

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
from datetime import datetime


shops = [11, 12, 13]
cashes = [1, 2, 3]

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
    "bread": "bakery",
    "butter": "dairy",
    "milk": "dairy",
    "chicken": "meat",
    "cereals": "cereals",
    "sugar": "groceries",
    "pork": "meat",
    "tomato": "vegetables",
    "onion": "vegetables",
    "tea": "beverages",
    "pasta": "groceries",
    "potato": "vegetables",
    "eggs": "dairy",
    "oil": "groceries",
    "fish": "seafood",
    "skyrim": "gaming",
}

prices = {
    "bread": 49,
    "butter": 129,
    "milk": 69,
    "chicken": 399,
    "cereals": 59,
    "sugar": 69,
    "pork": 449,
    "tomato": 149,
    "onion": 29,
    "tea": 89,
    "pasta": 69,
    "potato": 29,
    "eggs": 109,
    "oil": 119,
    "fish": 499,
    "skyrim": 1499,
}


def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return "".join(random.choice(letters) for _ in range(length))


def generate_data(shop_num, cash_num, num_rows):
    doc_ids = [generate_random_string(10) for _ in range(num_rows)]
    items_per_doc = {
        doc_id: random.sample(items, random.randint(1, len(items)))
        for doc_id in doc_ids
    }

    data = {
        "doc_id": [],
        "item": [],
        "category": [],
        "amount": [],
        "price": [],
        "discount": [],
    }

    for doc_id, item_list in items_per_doc.items():
        for item in item_list:
            price = prices[item]
            amount = np.random.choice(
                [1, 2, 3, 4, 5], p=[0.4, 0.225, 0.175, 0.15, 0.05]
            )
            discount = price * np.random.choice(
                [0, 0.05, 0.1, 0.15, 0.2], p=[0.5, 0.2, 0.15, 0.1, 0.05]
            )
            data["doc_id"].append(doc_id)
            data["item"].append(item)
            data["category"].append(categories[item])
            data["amount"].append(amount)
            data["price"].append(price)
            data["discount"].append(discount)

    df = pd.DataFrame(data)

    # Ensure directory exists
    os.makedirs("data", exist_ok=True)
    df.to_csv(f"data/{shop_num}_{cash_num}.csv", index=False)


# run script

if datetime.today().weekday() == 6:
    exit()

# Randomly choose 1 to 3 shops non-repeatable
# num_shops = random.randint(1, 3)
# selected_shops = random.sample(shops, num_shops)

for shop in shops:
    # Randomly choose 1 to 3 cashes non-repeatable for each shop
    num_cashes = random.randint(1, 3)
    selected_cashes = random.sample(cashes, num_cashes)

    for cash in selected_cashes:
        generate_data(
            shop, cash, random.randint(1, 5)
        )  # for a cash in a shop generates from 1 to 5 cheques
