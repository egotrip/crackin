###
'''
Write function that translates a text to Pig Latin and back. English is translated to Pig Latin by taking the first letter of every word, moving it to the end of the word and adding ‘ay’. “The quick brown fox” becomes “Hetay uickqay rownbay oxfay”.
'''

# move -> ovemay

def main():
	
	handle = take_input()
	# print(handle)
	latin = ' '.join(latin_string(handle))
	print(upper_first_letter(latin))




def take_input():
	''' No error checking '''
	print('Enter some string to translate: ')
	user_input = input()
	return user_input.split()


def latin_string(sentence):
	
	latin_sentence = []
	for word in sentence:
		word = word[1:] + word[0] + 'ay'
		latin_sentence.append(word)
	return latin_sentence

def upper_first_letter(s):
	s = s.lower()
	s = s[0].upper() + s[1:]
	return s


if __name__ == '__main__':
	main()
