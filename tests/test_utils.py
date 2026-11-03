import pytest
from learning_pandas.utils import greet


def test_greet_default():
    assert greet() == "Hello, Learner! Welcome to Learning Pandas."


def test_greet_custom():
    assert greet("Alice") == "Hello, Alice! Welcome to Learning Pandas."