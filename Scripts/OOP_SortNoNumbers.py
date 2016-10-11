""" Sorts the list by the reverse word order and in descending order
translate(str.maketrans('', '', '1234567890 ')) takes the dict
maketrans exchanges one sring to other letter by letter, and throws away the 3rd group
"""
# def letter_only(word):
# 	for symb in word:
# 		if symb.isalpha():
# 			word2 += symb
# 	return word2

def letter_only(word):
	return word.translate(str.maketrans('', '', '1234567890 '))

list1 = ['12 chairs', '2 tables', 'antique']
# list1.sort(key = for symb in word if symb.isalpha() word2 += symb)
#list1.sort(key = lambda x : x.translate(str.maketrans("", "", "1234567890 ")))
list1.sort(key = letter_only)
print(list1)