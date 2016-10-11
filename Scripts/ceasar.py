from string import ascii_lowercase
original = ascii_lowercase
shifter = original[4:] + original [:4]

encoder = dict(zip(original, shifter)) # tuples pairs from arguments and dict

text = raw_input('Please, enter text to encode: ')
encoded_text = ''

text.translate() # deletes special characters

for letter in text:
	encoded_text += encoder.get(letter, letter) # each string will be kept, very slow; 2nd letter for the special characters default value
	# if letter in encoder: 
 # 		encoded_text += encoder[letter]
 # 	else:
 # 		encoded_text += letter
print(encoded_text)