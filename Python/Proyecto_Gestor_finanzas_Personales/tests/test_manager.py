import pytest
from core.models import Category, Movement
from core.manager import Manager

def test_add_category_success():
    manager = Manager()
    category = Category("Food")

    manager.add_category(category)

    assert len(manager.categories) == 1
    assert manager.categories[0].name == "Food"


def test_add_duplicate_category():
    manager = Manager()
    manager.add_category(Category("Food"))

    with pytest.raises(ValueError):
        manager.add_category(Category("food"))

def test_add_movement_without_categories():
    manager = Manager()

    with pytest.raises(ValueError):
        manager.add_movement(
            "2025-01-01",
            "Lunch",
            10,
            "Food",
            "EXPENSE"
        )

def test_add_valid_movement():
    manager = Manager()
    manager.add_category(Category("Food"))

    manager.add_movement(
        "2025-01-01",
        "Lunch",
        10,
        "Food",
        "EXPENSE"
    )

    assert len(manager.movements) == 1
    assert manager.movements[0].title == "Lunch"

def test_total_incomes():
    manager = Manager()
    manager.add_category(Category("Job"))

    manager.add_movement("2025-01-01", "Salary", 1000, "Job", "INCOME")
    manager.add_movement("2025-01-02", "Bonus", 500, "Job", "INCOME")

    assert manager.total_incomes() == 1500

def test_total_expenses():
    manager = Manager()
    manager.add_category(Category("Food"))

    manager.add_movement("2025-01-01", "Lunch", 10, "Food", "EXPENSE")
    manager.add_movement("2025-01-02", "Dinner", 20, "Food", "EXPENSE")

    assert manager.total_expenses() == 30

def test_balance():
    manager = Manager()
    manager.add_category(Category("General"))

    manager.add_movement("2025-01-01", "Salary", 1000, "General", "INCOME")
    manager.add_movement("2025-01-02", "Rent", 400, "General", "EXPENSE")

    assert manager.balance() == 600
