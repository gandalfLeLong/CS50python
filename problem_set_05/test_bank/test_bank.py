from bank import value

def test100():
	assert value("erer") == 100

def test20():
	assert value("heheh") == 20

def test0():
	assert value("hello") == 0

def test_case_insensitive():
	assert value("HELLO") == 0
