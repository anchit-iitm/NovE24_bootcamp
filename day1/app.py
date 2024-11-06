from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

class test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    string = db.Column(db.String)
    boolean = db.Column(db.Boolean)
    num = db.Column(db.Integer)


with app.app_context():
    db.create_all()

# http status codes

@app.route('/', methods=['POST'])
def index():
    return 'Hello World'


@app.route('/homeNew')
def homeNew():
    var1 = 'kaushik'
    return jsonify({"nameFromPythonBackend":var1})   

@app.route('/multiJson')
def multiJson():
    var1 = 'kaushik'
    data = {"nameFromPythonBackend":var1}
    data2 = []
    for i in range(4):
        data2.append(data)
    print("data",data)
    print("data2",data2)
    return jsonify(data2)

@app.route('/test_post', methods=['POST'])
def test_post():
    # data = request.form['nameFromHtml']
    data = request.get_json()['nameFromHtml']
    print('data:', data)
    return "nameFromPythonBackend=data"

@app.route('/testJson', methods=['POST'])
def testJson():
    data = request.get_json()
    print('data:', data)
    print('string:', data["str"])
    print('bool:', data["bool"])
    print('num:', data["num"])
    return jsonify(data)


if __name__ == '__main__':
    app.run()