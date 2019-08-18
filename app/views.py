from app import app, render_template, request, redirect
from app import Backend,UPLOAD_DIR
from werkzeug.utils import secure_filename

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/action', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form 
        print(result)
        download = Backend(result)
        download.start()
        return redirect('/')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(UPLOAD_DIR+secure_filename(f.filename))
        return redirect('/')