usr_in = input()
default = [1, 1, 2, 2, 2, 8]

usr_in = [int(x) for x in usr_in.split()]
answer = []
for i in range(len(usr_in)):
	answer.append(default[i] - usr_in[i])

print(' '.join([str(w) for w in answer]))