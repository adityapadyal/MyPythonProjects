from flask import Flask, request
from flask_restful import Resource,Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.name

demoDatabase = {
    1:{'name':'Clean car'},
    2:{'name':'Write blog'},
    3:{'name':'Start stream'},
}

class Items(Resource):
    def get(self):

        return demoDatabase
    
    def post(self): 
        data = request.json
        itemId = len(demoDatabase.keys()) + 1
        demoDatabase[itemId] = {'name':data['name']}
        return demoDatabase

class Item(Resource):
    def get(self,pk):
        return demoDatabase[pk]

    def put(self,pk):
        data = request.json
        demoDatabase[pk]['name'] = data['name']
        return demoDatabase
    
    def delete(self, pk):
        del demoDatabase[pk]
        return demoDatabase

api.add_resource(Items,'/')
api.add_resource(Item, '/<int:pk>')

@app.route('/')

def hello():
    return '<h1>Hello, World! 123</h1>'

if __name__ == '__main__':
    app.run(debug=True,port=3000)
