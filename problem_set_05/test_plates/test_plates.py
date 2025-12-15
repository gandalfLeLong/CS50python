from plates import is_valid

def test_two_letters_start():
	assert is_valid("AA") == True
	assert is_valid("12") == False

def test_min_max():
	assert is_valid("A") == False
	assert is_valid("AAAAAAAAA") == False

def test_number():
	assert is_valid("AA1A") == False
	assert is_valid("AA01") == False
	assert is_valid("AA12") == True

def test_special_char():
	assert is_valid("AA-_+=") == False