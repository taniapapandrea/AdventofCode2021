file1 = open('input1.txt', 'r')
input1 = [x.strip() for x in file1.readlines()]

def process_oxygen_rating(input_list, digit):
	ones = ['1' for x in input_list if x[digit]=='1']
	common='1' if (len(ones) >= len(input_list)/2) else '0'
	input_list = [x for x in input_list if x[digit]==common]
	if len(input_list)==1:
		return input_list[0]
	else:
		return process_oxygen_rating(input_list, digit+1)

def process_co2_rating(input_list, digit):
	ones = ['1' for x in input_list if x[digit]=='1']
	uncommon='1' if (len(ones) < len(input_list)/2) else '0'
	input_list = [x for x in input_list if x[digit]==uncommon]
	if len(input_list)==1:
		return input_list[0]
	else:
		return process_co2_rating(input_list, digit+1)

oxygen_binary = process_oxygen_rating(input1, 0)
co2_binary = process_co2_rating(input1, 0)

oxygen_int = int(oxygen_binary, 2)
co2_int = int(co2_binary, 2)

print(oxygen_int*co2_int)