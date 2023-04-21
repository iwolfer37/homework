import pytest

from tree import Tree

def test_insert():
    tree = Tree()
    tree.insert(5)
    assert tree.data == 5

    tree.insert(3)
    assert tree.left.data == 3

    tree.insert(8)
    assert tree.right.data == 8

    tree.insert(4)
    assert tree.left.right.data == 4

    tree.insert(37)
    assert tree.right.right.data == 37

def test_remove():
    tree = Tree()
    data_list = [5, 3, 8, 4, 37, 11, 7, 6, 2]
    tree.insert_list(data_list)

    tree.remove(2)
    assert tree.min_value() == 3

    tree.remove(11)
    assert tree.max_value() == 37

    tree.remove(37)
    assert tree.right.data is None

def test_min_max_value():
    tree = Tree()
    data_list = [5, 3, 8, 4, 37, 11, 7, 6, 2]
    tree.insert_list(data_list)

    assert tree.min_value() == 2
    assert tree.max_value() == 37

    tree.remove(2)
    assert tree.min_value() == 3

    tree.remove(37)
    assert tree.max_value() == 11
