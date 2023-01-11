"""Flask app for Cupcakes"""
from flask import Flask, jsonify, request
from models import connect_db, db, Cupcake

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/api/cupcakes')
def list_cupcakes():
    """ Shows Lists of All Cupcakes """

    cupcakes = Cupcake.query.all()
    serialized = [cupcake.serialize() for cupcake in cupcakes]
    
    return (jsonify(cupcakes=serialized))


@app.route('/api/cupcakes', methods=['POST'])
def add_cupcake():
    """ Adds a New Cupcake to the DB """

    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image']

    cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(cupcake)
    db.session.commit()
    return (jsonify(cupcake=cupcake.serialize()), 201)


@app.route('/api/cupcakes/<int:id>')
def show_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return (jsonify(cupcake=cupcake.serialize()))

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def edit_cupcake(id):
    """ Edits Cupcake and Updates DB """

    cupcake = Cupcake.query.get_or_404(id)

    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image']

    cupcake.flavor = flavor
    cupcake.size = size
    cupcake.rating = rating
    cupcake.image = image

    db.session.add(cupcake)
    db.session.commit()

    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    """ Deletes Cupcake from DB """
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message='Deleted')


