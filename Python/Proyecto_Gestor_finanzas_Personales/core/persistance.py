import csv
import os
from core.models import Category, Movement

def load_categories(path):
    if not os.path.exists(path):
        return []

    categories = []

    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            categories.append(Category(row["name"]))

    return categories

def save_categories(path, categories):
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name"])
        for category in categories:
            writer.writerow([category.name])

def load_movements(path):
    if not os.path.exists(path):
        return []

    movements = []

    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            movements.append(
                Movement(
                    row["date"],
                    row["title"],
                    row["amount"],
                    row["category"],
                    row["type"]
                )
            )

    return movements

def save_movements(path, movements):
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "title", "amount", "category", "type"])
        for m in movements:
            writer.writerow([
                m.date,
                m.title,
                m.amount,
                m.category,
                m.type
            ])


