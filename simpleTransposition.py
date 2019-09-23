###
# Write a code which encrypts a string using the simple transposition method.
# In this method you should create 2 new strings 
# and put even-indexed characters (including index 0) to the first 
# and odd-indexed ones to the second. Next concatenate the strings.
# Example: 
# simpleTransposition("abab12") -> "aa1bb2"
# Input: input string S
# Output: string S after encryption
# Constraints 0 < length of S < 1000
####################
####################
# STEPS #




def stringCheck(S):
	if (len(S) > 0 and len(S) < 1000):
		return True
	return False


def simpleTransposition(S):
	lst = ['', '']

	i = 0
	while len(S) > i:
		# even-indexed letters including 0
		if (i % 2 == 0):
			lst[0] += S[i]
		else:
			lst[1] += S[i]
		i += 1
	print(f'Before: {S}\nAfter: {lst[0] + lst[1]}')



def main():

	test_string = 'test string'
	if (stringCheck(test_string)):
		simpleTransposition(test_string)

if __name__ == '__main__':
	main()
