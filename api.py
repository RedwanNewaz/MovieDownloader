from config import app, render_template, request, redirect,Backend
from werkzeug.utils import secure_filename
from time import time
from datetime import datetime
from flask import jsonify
import json, os


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/action', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        req = request.form 
        

        # using global parameter from __main__
        result = {'option':req.get('option')}
        for p in req:result[p]=req[p]
        for p in parameter:result[p]=parameter[p]
        download = Backend(result)
        download.start()
        return redirect('/')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(parameter["dir_download"]+"/"+secure_filename(f.filename))
        return redirect('/')

@app.route('/info')
def debug_msg():
 
    file = parameter["dir_log"]+"/log.json"
    with open(file) as data:
        data = data.read()
        data = json.loads(data)
    filesize = lambda file : (os.path.getsize(file)*10485>>20)/10000.0 if os.path.exists(file) else 0
    for d in data:
        d['size'] = "{} MB".format(filesize(d['file']))
        d['file'] = d['file'].split('/')[-1]
    return render_template('record.html', records=data, colnames=['file','start_time','finish_time','size'])


if __name__=="__main__":
    with open("config/config.json") as param:
        param = param.read()
        parameter = json.loads(param)
    app.run(host=parameter["ip"], port=parameter["port"], debug=True)