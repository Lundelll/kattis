numbers = input()
temps = input().split()
answer = 0

for x in temps:
	if(int(x) < 0):
		answer += 1

print(answer)