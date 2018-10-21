#Library
from flask import *
from werkzeug.security import safe_join
import subprocess
import os

import mylibrary

#Variable
measure_proc = None

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

@app.route('/mereni_start')
def get_mereni_start():
	global measure_proc
	
	if measure_proc is None:
		return render_template('mereni_start.html', text='Neprobiha zadne mereni')

	return render_template('mereni_start.html', text='Probiha mereni')

@app.route('/mereni_start', methods=['POST'])
def get_mereni_start_button():
	global measure_proc
	actual_time="Mereni zastaveno "
	actual_time += mylibrary.get_actual_time()
	
	#stop measurement
	if not measure_proc is None:
		measure_proc.terminate()
		return render_template('mereni_start.html', text=actual_time)
	return render_template('mereni_start.html', text='Neprobiha zadne mereni')

@app.route('/mereni_stop')
def get_mereni_stop():
	global measure_proc

	if measure_proc is None:
		return render_template('mereni_stop.html', text="Neprobiha zadne mereni")

	return render_template('mereni_stop.html', text="Probiha mererni")

@app.route('/mereni_stop', methods=['POST'])
def get_mereni_stop_button():
	global measure_proc
	actual_time = "Mereni spusteno "
	actual_time += mylibrary.get_actual_time()
	
	#run measurement
	measure_proc = subprocess.Popen(['python3', 'measure.py'])
	return render_template('mereni_stop.html', text=actual_time)

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
    return render_template("graph.html")
