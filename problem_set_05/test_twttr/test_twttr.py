from twttr import shorten

def test_upper_A():
	assert shorten("A") == ""

def test_upper_E():
	assert shorten("E") == ""

def test_upper_I():
	assert shorten("I") == ""

def test_upper_O():
	assert shorten("O") == ""

def test_upper_U():
	assert shorten("U") == ""

def test_upper_a():
	assert shorten("a") == ""

def test_upper_e():
	assert shorten("e") == ""

def test_upper_i():
	assert shorten("i") == ""

def test_upper_o():
	assert shorten("o") == ""

def test_upper_u():
	assert shorten("u") == ""

def test_no_vowel():
	assert shorten("BLKJqsd") == "BLKJqsd"

def test_multiple_vowel():
	assert shorten("Coucou C'est CHARLIE") == "Cc C'st CHRL"

def test_numbers():
	assert shorten("0123456789") == "0123456789"

def test_symbols():
	assert shorten(",;:?./+=-_)(\'\"&@<>") == ",;:?./+=-_)(\'\"&@<>"