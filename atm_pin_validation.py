###
'''
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. Your task is to create a function that takes a string and returns True if the PIN is valid and False if it's not.
'''
# isnumeric() lol

def main():
	

	digits = take_input()
	result = check_input(digits)

	if (result):
		print('PIN code is correct!')
	else: 
		print('Wrong code! Try again!')



def take_input():
	print('Provide 4 or 6 digits PIN code: ')
	raw_input = input()

	return raw_input


def check_input(sequence):
	if ((len(sequence) == 4 or len(sequence) == 6) and sequence.isnumeric()):
		return True
		

if __name__ == '__main__':
	main()
