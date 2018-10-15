from random import randint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def randomNumbers():
	numbers = [1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 25., 50., 75., 100.]
	randomNumbers = []

	for i in range (0, 6):
		randomNumbers.append(numbers[randint(0, 13)])

	return randomNumbers


def computation(a, b, i):
	if i == 0:
		if a + b == int(a + b) and a + b >= 0:
			print a,
			print '+',
			print b,
			print '=',

		return a + b

	elif i == 1:
		if a - b == int(a - b) and a - b >= 0:
			print a,
			print '-',
			print b,
			print '=',

		return a - b
	elif i == 2:
		if a * b == int(a * b) and a * b >= 0:
			print a,
			print '*',
			print b,
			print '=',

		return a * b

	elif i == 3:
		if a / b == int(a / b) and a / b >= 0:
			print a,
			print '/',
			print b,
			print '=',

		return a / b

results = []

def algo(numbers):
	if len(numbers) >= 2:
		for j in range(0, len(numbers)):
			if j < len(numbers)-1:
				print bcolors.UNDERLINE
				print numbers[j],
			else:
				print numbers[j]
				print bcolors.ENDC
		print ''

		for i in range(0, 4):
			res = computation(numbers[0], numbers[1], i)
			results.append(res)
			if res == int(res) and res >= 0:
				print res

				newNumbers = numbers[2:]
				newNumbers = [res] + newNumbers

				print ''


				algo(newNumbers)
			else:
				print ''



number = randint(101, 999)

numbers = randomNumbers()
numbers = [8., 10., 3., 4., 7., 2.]

print number
for i in range(0, len(numbers)):
	if i < len(numbers)-1:
		print numbers[i],
	else:
		print numbers[i]

print ''

algo(numbers)

print len(results)