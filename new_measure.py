import subprocess
import mylibrary
import os
import threading


def measurement(action):
	global measure_proc
	global thread

	if action is "start":
		measure_proc=subprocess.Popen('utils/generator', stdout=subprocess.PIPE)
		thread = threading.Thread(target=data_saving)
		thread.start()
		
	if action is "stop":
		if measure_proc.poll() is not None:
			thread.do_run = False
			thread.join()
			measure_proc.terminate()
				if measure_proc.poll() is not None:
					return True

		else:
			return False

def data_saving():
	global measure_proc

	path = os.path.join('/', 'home', 'mplch', 'web', 'measures', mylibrary.get_date_name() + ".txt")
	fmeasure = open(path, "w")
	t = threading.currentThread()
	while getattr(t, "do_run", True):
		line = measure_proc.stdout.readline()
		line = line.decode()
		if line[0] == "2":
			fmeasure.write(line)

	fmeasure.close()
	
def is_running():
	global measure_proc

	if measure_proc is None:
		return False

	else:
		return True

#Vraci aktualni cas, pokud se povede spustit vlakno, jinak 'None'
def mstart():
	global measure_proc

	if measure_proc is None:
		start=measurement("start")
		if start is True:
			return mylibrary.get_actual_time()

		else:
			return None

#Vraci aktualni cas, pokud se povede ukoncit vlakno, jinak 'None'
def mstop():
	global measure_proc

	if measure_proc is not None:
		stop=measurement("stop")
		if stop is True:
			return mylibrary.get_actual_time()
		
		else:
			return None
