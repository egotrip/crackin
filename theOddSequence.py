###
# Write a code which finds the integer number that appears
# an odd number of times in the given sequence.
# Input: S - the given sequence of numbers separated with spaces
# Output: the sequence of searched numbers
# Constraints:
# 0 <= length of S <= 1000
# 0 <= max value of numbers in S <= 1000

import random


def generateNumList():
	''' Generate list of random numbers, up to 1000 elements.'''
	lst = []
	lst_lenght = random.randint(10, 1000)
	i = 0
	while i < lst_lenght:
		lst.append(random.randint(0, 9)) 
		i += 1
	return lst

def count_appearences(lst):
	''' Count how many times each number appeared in the list.
	Returns dictionary.'''
	count_dict = {}
	for num in lst:
		if num in count_dict.keys():
			count_dict[num] += 1
		else:
			count_dict[num] = 1
	return count_dict

def only_odd_values(d):
	odd_dict = {}
	for key, value in d.items():
		if not value % 2 == 0:
			odd_dict[key] = value
	return odd_dict


def main():

	test_lst = generateNumList()
	print(f'Length of the list: {len(test_lst)}')
	
	d = count_appearences(test_lst)
	for key, value in d.items():
		print(f'{key}: {value}')
	print(sum(d.values()))
	odd = only_odd_values(d)
	print(odd)



if __name__ == '__main__':
	main()
