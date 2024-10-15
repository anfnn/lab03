import pytest
from main import bubble_sort

def test_bubble_sort_ascending():
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr, ascending=True)
    assert arr == [11, 12, 22, 25, 34, 64, 90]

def test_bubble_sort_descending():
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr, ascending=False)
    assert arr == [90, 64, 34, 25, 22, 12, 11]

def test_bubble_sort_empty():
    arr = []
    bubble_sort(arr, ascending=True)
    assert arr == []

def test_bubble_sort_single_element():
    arr = [42]
    bubble_sort(arr, ascending=True)
    assert arr == [42]
