from math import pi

def get_closest_pair():
	'''
	Returns a tuple, numerator and denominator
	ratio of the two is as close to pi as possible
	'''
	target = pi
	best_num = 1.
	best_denom = 1.
	tempDenom = 1.0
	tempNum = None

	while tempDenom <= 333.0:
		tempNum = tempDenom * 3
		upper_limit = tempDenom * 3.5
		while tempNum < 1000.0 and tempNum < upper_limit:
			if abs((tempNum / tempDenom) - target) < abs((best_num / best_denom) - target):
				best_num = tempNum
				best_denom = tempDenom
			tempNum += 1
		tempDenom += 1

	return best_num, best_denom

def main():
	closest_pair = get_closest_pair()

	print 'Best pair = {}, {}'.format(*closest_pair)
	print 'ratio = {}'.format(closest_pair[0] / closest_pair[1])

if __name__ == '__main__':
	main()
