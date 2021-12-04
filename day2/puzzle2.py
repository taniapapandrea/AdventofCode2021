file1 = open('input.txt', 'r')
input1 = [x.strip() for x in file1.readlines()]

p_horizontal = 0
p_depth = 0
aim = 0

for i in input1:
	direction, distance = i.split()
	if direction == 'forward':
		p_horizontal += int(distance)
		p_depth += int(distance)*aim
	elif direction == 'down':
		aim += int(distance)
	elif direction == 'up':
		aim -= int(distance)

print(p_horizontal*p_depth)