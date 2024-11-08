from flask import Flask, jsonify, request, make_response
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

@app.route('/')
def index():
    return 'Hello World'


@app.route('/homeNew')
def homeNew():
    var1 = 'kaushik'
    return jsonify({"nameFromPythonBackend":var1}), 201 

@app.route('/homeNew1')
def homeNew1():
    var1 = 'kaushik'
    return make_response(jsonify({"nameFromPythonBackend":var1}), 201)   

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

@app.route('/store', methods=['POST'])
def store():
    data = request.get_json()
    new_row = test(string=data['str'], boolean=data['bool'], num=data['num'])
    db.session.add(new_row)
    db.session.commit()
    return jsonify({'message': 'success', "id": new_row.id})

@app.route('/retrieve')
def retrieve():
    dataFromDb = test.query.filter_by(id=1).first()
    return jsonify({'message': 'success', "id": dataFromDb.id, "str": dataFromDb.string, "bool": dataFromDb.boolean, "num": dataFromDb.num})

@app.route('/retrieve/<idFromPath>')
def retrievePath(idFromPath):
    dataFromDb = test.query.filter_by(id=idFromPath).first()
    return jsonify({'message': 'success', "id": dataFromDb.id, "str": dataFromDb.string, "bool": dataFromDb.boolean, "num": dataFromDb.num})

@app.route('/retrieveJson')
def retrieveJson():
    passedId = request.get_json()["idFromJson"]
    dataFromDb = test.query.filter_by(id=passedId).first()
    return jsonify({'message': 'success', "id": dataFromDb.id, "str": dataFromDb.string, "bool": dataFromDb.boolean, "num": dataFromDb.num})

@app.route('/storeNew', methods=['POST', 'PUT', 'DELETE', 'GET']) # changed in day2
def storeNew():
    if request.method == "POST":
        data = request.get_json()
        new_row = test(string=data['str'], boolean=data['bool'], num=data['num'])
        db.session.add(new_row)
        db.session.commit()
        return make_response(jsonify({'message': 'success', "id": new_row.id}), 201)
    if request.method == "PUT":
        data = request.get_json()
        row = test.query.filter_by(id=data['idFromJson']).first()
        row.string = data['str']
        row.boolean = data['bool']
        row.num = data['num']
        db.session.commit()
        return make_response(jsonify({'message': 'success', "id": row.id}), 202)
    if request.method == "DELETE":
        data = request.get_json()
        row = test.query.filter_by(id=data['idFromJson']).first()
        if row is None:
            return make_response(jsonify({'message': 'error', "id": data['idFromJson']}), 404)
        db.session.delete(row)
        db.session.commit()
        return make_response(jsonify({'message': 'success', "id": row.id}), 202)
    # changed in day2
    if request.method == "GET":
        passedId = request.get_json()
        print(passedId, type(passedId))
        dataFromDb = test.query.filter_by(id=passedId["idFromJson"]).first()
        return jsonify({'message': 'success', "id": dataFromDb.id, "str": dataFromDb.string, "bool": dataFromDb.boolean, "num": dataFromDb.num})

# @app.route('/update', methods=['POST'])
# @app.route('/update', methods=['PATCH'])
@app.route('/update', methods=['PUT'])
def update():
    data = request.get_json()
    # new_row = test(string=data['str'], boolean=data['bool'], num=data['num'])
    # db.session.add(new_row)
    row = test.query.filter_by(id=data['idFromJson']).first()
    row.string = data['str']
    row.boolean = data['bool']
    row.num = data['num']
    db.session.commit()
    return jsonify({'message': 'success', "id": row.id})

# @app.route('/update', methods=['POST'])
# @app.route('/update', methods=['PATCH'])
@app.route('/delete', methods=['DELETE']) # changed in day2
# @app.route('/delete', methods=['PUT']) # changed in day2
def delete():
    data = request.get_json()
    row = test.query.filter_by(id=data['idFromJson']).first()
    if row is None:
        return jsonify({'message': 'error', "id": data['idFromJson']})
    db.session.delete(row)
    db.session.commit()
    return jsonify({'message': 'success', "id": row.id})

if __name__ == '__main__':
    app.run()