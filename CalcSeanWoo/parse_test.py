import pytest
from Calculate import *


def test_add_1():
    assert parse("2+6") == 8.0
def test_add_2():
    assert parse("-2+6") == 4.0
def test_add_3():
    assert parse("4+-2+6") == 8.0
def test_add_4():
    assert parse("2+6+-2") == 6.0
def test_add_5():
    assert parse("53+45+1+1") == 100.0

def test_sub_1():
    assert parse("2-6") == -4.0
def test_sub_2():
    assert parse("-2-6") == -8.0
def test_sub_3():
    assert parse("-2-6-100") == -108.0
def test_sub_4():
    assert parse("2-6-2") == -6.0
def test_sub_5():
    assert parse("53-45-1-1") == 6.0
