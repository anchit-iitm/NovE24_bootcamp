from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

print('app.py __name__:', __name__)
print('updated new app.py')

@app.route('/')
def index():
    return 'Hello World'


@app.route('/home')
def home():
    return render_template('hello.html')

@app.route('/homeNew')
def homeNew():
    var1 = 'kaushik'
    return render_template('helloNew.html', nameFromPythonBackend=var1)

@app.route('/postEndpoint', methods=['POST', 'GET'])
def postPyFn():
    if request.method == 'POST':
        print('post request')
        data = request.form['nameFromHtml']
        print('data:', data)
        return render_template('helloNew_withpost.html', nameFromPythonBackend=data)
    if request.method == 'GET':
        print('get request')
        return render_template('helloNew_withpost.html', nameFromPythonBackend='please supply')
    # 


if __name__ == '__main__':
    app.run()