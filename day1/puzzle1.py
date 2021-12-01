file1 = open('input.txt', 'r')
## Fun fact: if you don't cast to int(x), python thinks that "1003\n" < "985\n"
numbers = [int(x) for x in file1.readlines()]

count = 0
l = len(numbers)

for i in range(1, l):
	num = numbers[i]
	prev = numbers[i-1]
	if (num > prev):
		count += 1
		print('{} increased from {}. count={}\n'.format(num, prev, count))
	else:
		print('{} decreased from {}. count={}\n'.format(num, prev, count))