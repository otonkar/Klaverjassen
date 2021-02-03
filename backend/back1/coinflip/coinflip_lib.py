#coinflip/coinflip_lib.py

#####
##
## The file belongs to the coinflip App for calulating the chances
##
####


def pascal_triangle(n):
	'''
	Get pascals triange for n flips of a coins.
	   		         	1
	n=1				1		1
	n=2			1		2		1
	n=3		1		3		3		1

	This array can be used to calculate the chance of a certain outcome.
			
	'''

	array = [1]
	y = [0]

	for x in range(max(n,0)):
		array = [l+r for l,r in zip(array + y, y + array)]

	return array


def calc_chance(n, r):
	'''
	Given an experiment of n flips of a coin, resulting in r positive outcomes (like heads)
	This function calculates the chance that a next experiment gives the same result or better.

	It caculates the som for P(r) + P(r+1) +  .... P(n)


	'''
	# Fair coin
	p = 0.5

	array = pascal_triangle(n)
	chance = sum(array[r:]) / sum(array)

	# max 8 decimal places
	chance = round(chance, 8)

	return chance




