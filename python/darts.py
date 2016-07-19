import math


cases = input()

for case in range(int(cases)):
	throws = input()
	points = 0

	for x in range(int(throws)):
	throw = input()
	throw = throw.split()
	radius = math.sqrt((int(throw[0]) ** 2) + (int(throw[1]) ** 2))

	if radius <= 20:
		points += 10
	elif radius <= 40:
		points += 9
	elif radius <= 60:
		points += 8
	elif radius <= 80:
		points += 7
	elif radius <= 100:
		points += 6
	elif radius <= 120:
		points += 5
	elif radius <= 140:
		points += 4
	elif radius <= 160:
		points += 3
	elif radius <= 180:
		points += 2
	elif radius <= 200:
		points += 1
	else:
		points += 0

	print(points)