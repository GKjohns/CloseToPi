from math import pi

target = pi

bestpair = {"num" : 1.0, "denom" : 1.0}

tempDenom = 1.0
tempNum = None

while tempDenom <= 333.0:

	tempNum = tempDenom * 3

	while tempNum < 1000.0 and tempNum < tempDenom * 4:

		if pow((tempNum / tempDenom) - target, 2) < pow((bestpair["num"] / bestpair["denom"]) - target, 2):

			bestpair["num"] = tempNum
			bestpair["denom"] = tempDenom
		
		tempNum += 1

	tempDenom += 1

print "Numerator: {}\nDenominator: {}".format(bestpair["num"], bestpair["denom"])

