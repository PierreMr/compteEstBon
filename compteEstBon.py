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
		# if a + b == int(a + b):
		# 	print a,
		# 	print '+',
		# 	print b,
		# 	print '=',

		return a + b

	elif i == 1:
		# if a - b == int(a - b):
		# 	print a,
		# 	print '-',
		# 	print b,
		# 	print '=',

		return abs(a - b)
	elif i == 2:
		# if a * b == int(a * b):
		# 	print a,
		# 	print '*',
		# 	print b,
		# 	print '=',

		return a * b

	elif i == 3:
		# if a / b == int(a / b):
		# 	print a,
		# 	print '/',
		# 	print b,
		# 	print '=',
	
		# 	return a / b
		# elif b / a == int(b / a):
		# 	print a,
		# 	print '/',
		# 	print b,
		# 	print '=',
	
		# 	return b / a
		# else:
			
		# 	return a / b
		return a / b

def change(array, a, b):
	temp = array[a]
	array[a] = array[b]
	array[b] = temp

	return array

computations = []
results = []

def algo(numbers):
	if len(numbers) >= 2:
		# for j in range(0, len(numbers)):
		# 	if j < len(numbers)-1:
		# 		print bcolors.UNDERLINE,
		# 		print numbers[j],
		# 	else:
		# 		print numbers[j]
		# 		print bcolors.ENDC
		# print ''

		for i in range(0, 4):
			res = computation(numbers[0], numbers[1], i)
			computations.append(res)

			if res == number:
				string = str(numbers[0])
				if i == 0:
					string += ' + '
				if i == 1:
					string += ' - '
				if i == 2:
					string += ' * '
				if i == 3:
					string += ' / '
				string += str(numbers[1])
				string += ' = '
				string += str(res)

				results.append(string)

			if res == int(res) and res >= 0:
				# print res

				newNumbers = numbers[2:]
				newNumbers = [res] + newNumbers

				# print ''
				algo(newNumbers)
			else:
				# print ''
				algo(newNumbers)



number = randint(101, 999)
# number = 112

numbers = randomNumbers()
# numbers = [64., 32., 16., 8., 4., 2.]

print number
for i in range(0, len(numbers)):
	if i < len(numbers)-1:
		print numbers[i],
	else:
		print numbers[i]
		print ''

# for n in range(0, len(numbers)):
# 	algo(numbers)
	
# 	temp = numbers[0]
# 	numbers = numbers[1:]
# 	numbers = numbers + [temp]

for z in range(0, 6):
	if z > 0 and z < 3:
		numbers = change(numbers, 0, 1)
	elif z == 3:
		numbers = change(numbers, 0, 3)
	elif z == 4:
		numbers = change(numbers, 0, 4)
	elif z == 5:
		numbers = change(numbers, 0, 5)
	
	for y in range(0, 5):
		if y > 0:
			numbers = change(numbers, 1, 2)
		
		for x in range(0, 4):
			if x > 0 and x != 3:
				numbers = change(numbers, 2, 3)
			elif x == 3:
				numbers = change(numbers, 2, 5)
			
			for w in range(0, 3):
				if w > 0:
					numbers = change(numbers, 3, 4)
			
				for v in range(0, 2):
					if v > 0:
						numbers = change(numbers, 4, 5)

						algo(numbers)

print len(computations)

print ''

for i in range(0, len(results)):
	print results[i]

print ''

print len(results)