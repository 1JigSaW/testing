def test_substring(full_string, substring):
	index = full_string.find(substring)
	assert index != -1, f"expected '{substring}' to be substring of '{full_string}'"