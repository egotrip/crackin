###
# Takes a list of strings and prints them, one per line in rectangular frame.

lst = ['action',
	'activity',
	'actually',
	'add',
	'administratio1',
	'address',
	'administration',
	'authenticationofthefuckinfinest']

### MAIN ###
def main():
	
	display(lst)


### ENDMAIN ###


def longest_word(lst_of_words):

	longest = ''
	for word in lst_of_words:
		if(len(word) > len(longest)):
			longest = word
	return longest


def display(lst_of_words):
	# holy szmoly it works !!
	longest = len(longest_word(lst_of_words)) + 4

	print(longest*'*')
	for word in lst_of_words:
		space = (longest - 4) - len(word)
		print('* ' + word + space*' ' + ' *')
	print(longest*'*')




if __name__ == '__main__':
	main()
