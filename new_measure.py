import subprocess
import mylibrary
import os

global measure_proc


def measurement(action):
	if action is "start"
		measure_proc=subprocess.Popen('utils/generator', stdout=subprocess.PIPE)
		if measure_proc.poll() is None
			return True
		
	if action is "stop"
		if measure_proc.poll() is not None
			measure_proc.terminate()
				if measure_proc.poll() is not None
					return True
def is_running():
	if measure_proc is None:
	return False
	else:
	return True

#Vraci aktualni cas, pokud se povede spustit vlakno, jinak 'None'
def mstart():
	if measure_proc is None:
		start=measurement("start")
		if start is True
			return mylibrary.get_actual_time()
		else:
			return None

#Vraci aktualni cas, pokud se povede ukoncit vlakno, jinak 'None'
def mstop():
	if measure_proc is not None:
		stop=measurement("stop")
		if stop is True
			return mylibrary.get_actual_time()
		else:
			return None
