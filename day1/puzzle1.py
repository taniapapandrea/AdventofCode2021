### This returns one number too small

file1 = open('input.txt', 'r')
numbers = file1.readlines()

count = 0
l = len(numbers)

for i in range(l):
	num = numbers[i]
	prev = numbers[i-1]
	if (num > prev):
		count += 1
		print('{} increased from {}. count={}\n'.format(num, prev, count))
	else:
		print('{} decreased from {}. count={}\n'.format(num, prev, count))