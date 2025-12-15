from fuel import convert, gauge
import pytest

def test_zero_div():
	with pytest.raises(ZeroDivisionError):
		convert("1/0")

def test_not_int():
	with pytest.raises(ValueError):
		convert("aa/aa")

def test_x_greater_than_y():
	with pytest.raises(ValueError):
		convert("4/3")

def test_negative():
	with pytest.raises(ValueError):
		convert("-1/2")

def test_wrong_int():
	assert convert("1/2") == 50

def test_empty():
	assert gauge(1) == "E"

def test_full():
	assert gauge(99) == "F"

def test_value():
	assert gauge(51) == "51%"