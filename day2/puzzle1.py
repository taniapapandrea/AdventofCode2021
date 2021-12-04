file1 = open('input.txt', 'r')
input1 = [x.strip() for x in file1.readlines()]

p_horizontal = 0
p_depth = 0

for i in input1:
	direction, distance = i.split()
	if direction == 'forward':
		p_horizontal += int(distance)
	elif direction == 'down':
		p_depth += int(distance)
	elif direction == 'up':
		p_depth -= int(distance)

print(p_horizontal*p_depth)