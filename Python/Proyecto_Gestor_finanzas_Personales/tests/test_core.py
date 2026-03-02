import pytest
from core.models import Category
from core.models import Movement

def test_category_trim():
    cat = Category("  Food  ")
    assert cat.name == "Food"

def test_category_empty():
    with pytest.raises(ValueError):
        Category("  ")

def test_movement_valid():
    move = Movement("2025-09-20", "Salary", 1000, "Work", "INCOME")
    assert move.amount == 1000

