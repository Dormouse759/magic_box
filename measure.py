import subprocess
import mylibrary
import datetime
import os


sub_dir = mylibrary.init_var()
file_cnt = 1

measure_proc = subprocess.Popen(["/fs1/fpga_cnt/ttmeas_v6", "-vd", "-c 2"], stdout = subprocess.PIPE)
path = os.path.join(os.getcwd(), "measures", str(sub_dir))
os.mkdir(path)
if not os.path.exists(path):
	print ("soubor nejde vytvorit")
	quit()

while True:
	path = os.path.join(os.getcwd(), "measures", str(sub_dir), str(file_cnt) + ".txt")
	file = open(path, "w")
	file.write("[\n")

	meas_cnt = 0
	while True:
		if meas_cnt == 3600:
			break
		line = measure_proc.stdout.readline()
		line = line.decode()
		if line[0] == "2":
			timestamp, value = mylibrary.separate_values(line)
			date = timestamp.split(".")[0]
			file.write("[ " + date + ", " + value + "],\n")
			meas_cnt += 1
	file.write("]")
	file_cnt += 1
measure_proc.terminate()
file.close()
