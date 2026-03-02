import random
import pytest
from order_algorithms.bubble_sort import bubble_sort

def test_bubble_sort_works_with_small_list():
    #arrange
    small_list = [10, 8, 85, 78, 56, 14, 95, 32, 1, 6]
    #act
    result = bubble_sort(small_list)
    #Assert
    assert result == [1, 6, 8, 10, 14, 32, 56, 78, 85, 95]

def test_bubble_sort_works_with_big_list_more_than_100_elements():
    #arrange
    big_list_ordered = list(range(101))
    random.shuffle(big_list_ordered)
    #act
    result = bubble_sort(big_list_ordered)
    #Assert
    assert result == list(range(101))

def test_bubble_sort_works_with_empty_list():
    #arrange
    empty_list = []
    #act
    result = bubble_sort(empty_list)
    #Assert
    assert result == []

def test_bubble_sort_crash_with_no_list_parameters():
    #arrange
    no_list = {"a":"8"}
    #act & assert
    with pytest.raises(TypeError):
        bubble_sort(no_list)