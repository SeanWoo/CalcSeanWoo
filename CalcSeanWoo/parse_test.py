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


def test_mul_1():
    assert parse("2*6") == 12.0
def test_mul_2():
    assert parse("-2*6") == -12.0
def test_mul_3():
    assert parse("-2-6*100") == -602.0
def test_mul_4():
    assert parse("2*6-2") == 10.0
def test_mul_5():
    assert parse("53*45-1+1") == 2385.0



def test_div_1():
    assert parse("6/2") == 3.0
def test_div_2():
    assert parse("6/-2") == -3.0
def test_div_3():
    assert parse("-2-6/100") == -2.06
def test_div_4():
    assert parse("12/6-2") == 0
def test_div_5():
    assert parse("-10/2") == -5

def test_mod_1():
    assert parse("100-10^-2") == 99.99
def test_mod_2():
    assert parse("100+10^-2") == 100.01
def test_mod_3():
    assert parse("100-10^2") == 0.0
def test_mod_4():
    assert parse("100+10^2") == 200.0

def test_mod_5():
    assert parse("100-10^-3") == 99.999
def test_mod_6():
    assert parse("100+10^-3") == 100.001
def test_mod_7():
    assert parse("100-10^3") == -900.0
def test_mod_8():
    assert parse("100+10^3") == 1100.0

def test_mod_9():
    assert parse("100-10^-4") == 99.9999
def test_mod_10():
    assert parse("100+10^-4") == 100.0001
def test_mod_11():
    assert parse("100-10^4") == -9900.0
def test_mod_12():
    assert parse("100+10^4") == 10100.0