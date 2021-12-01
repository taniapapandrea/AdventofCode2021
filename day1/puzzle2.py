file1 = open('input.txt', 'r')
numbers = [int(x) for x in file1.readlines()]

count = 0
l = len(numbers)

for i in range(0, l-3):
	num = numbers[i] + numbers[i+1] + numbers[i+2]
	next = numbers[i+1] + numbers[i+2] + numbers[i+3]
	if (next > num):
		count += 1

print(count)