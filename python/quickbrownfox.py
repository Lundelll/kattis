rows = input()
for i in range(int(rows)):
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	line = input()
	for c in line.lower():
		if c in alphabet:
			alphabet.remove(c)

	if len(alphabet) < 1:
		print('pangram')
	else:
		print('missing', str.join('', alphabet))
