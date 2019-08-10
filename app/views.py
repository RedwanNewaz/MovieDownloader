from app import app, render_template, request, redirect
from app import Backend

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