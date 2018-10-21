import datetime
import os


def get_actual_time():
	now = datetime.datetime.now()
	now = now.strftime("%d.%m.%Y %H:%M:%S")
	return now

def separate_values(line):
	line = line.strip()
	line = line.split(" ")
	return line[1], line[-2]

def convert_to_date(timestamp):
	timestamp = timestamp.split(".")
	date = datetime.datetime.fromtimestamp(int(timestamp[0] + timestamp[1]))
	date = date.strftime("%d-%m-%Y_%H:%M:%S")
	return date

def init_var():
	path = os.path.join(os.getcwd(), "measures")
	file_list = os.listdir(path)
	file_list = list(map(int, file_list))
	sub_dir = get_max(file_list)
	sub_dir += 1
	return sub_dir

def get_max(int_list):
	max = 0
	for number in int_list:
		if number > max:
			max = number
	return max
