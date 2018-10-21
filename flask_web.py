#Library
from flask import *
from werkzeug.security import safe_join
import subprocess
import os

import mylibrary

#Variable
measure_proc = None
measure_start_date = "Neprobiha zadne mereni "

# -> Start
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('DIFF_SETTINGS', silent=True)

# Web
@app.route('/')
def index():
	return redirect(url_for('get_index'))

@app.route('/index')
def get_index():
	return render_template('index.html', time=mylibrary.get_actual_time())

@app.route('/mereni')
def get_mereni():
	global measure_proc
	global measure_start_date

	if measure_proc is None:
		return render_template('mereni.html', text=measure_start_date, button='Start')

	return render_template('mereni.html', text=measure_start_date, button='Stop')

@app.route('/mereni', methods=['POST'])
def get_mereni_button():
	global measure_proc
	global measure_start_date
	
	if measure_proc is None:
		measure_start_date = "Mereni probiha od "
		measure_start_date += mylibrary.get_actual_time()
	
		#run measurement
		measure_proc = subprocess.Popen(['python3', 'measure.py'])
		return render_template('mereni.html', text=measure_start_date, button='Stop')
	else:
		measure_start_date = "Mereni zastaveno "
		measure_start_date += mylibrary.get_actual_time()
		
		#stop measurement
		measure_proc.terminate()
		measure_proc = None
		return render_template('mereni.html', text=measure_start_date, button='Start')

@app.route('/measures')
@app.route('/measures/<sub_dir>')
@app.route('/measures/<sub_dir>/<file_name>')
def get_directory(sub_dir=None, file_name=None):
	dir_name = 'measures'
	path = dir_name
	
	if not sub_dir is None:
		path = safe_join(dir_name, sub_dir)
		if not file_name is None:
			path = safe_join(path, file_name)
			if os.path.isfile(path): return get_graph()

	if path is None:
		abort(404)

	files = os.listdir(path)
	return render_template('soubory.html', files=files, sub_dir=sub_dir, file_name=file_name, path=path)

@app.route('/return_file/measures/<sub_dir>/<file_name>')
def return_file(sub_dir, file_name):
	return send_file(os.path.join('measures', sub_dir, file_name), as_attachment=True)

@app.route('/graph')
def get_graph():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
 
    return render_template("graph.html", values=values, labels=labels)
