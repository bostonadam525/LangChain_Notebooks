# import flask, sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

# Create a new Flask instance
app = Flask(__name__)
# set config for sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# define the Api
api = Api(app)

# Create a new model for the database
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    # represent class
    def __repr__():
        return f"User(name = {self.name}, email = {self.name})"


# Create user arguments
user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True, help="Name cannot be blank")
user_args.add_argument('email', type=str, required=True, help="Email cannot be blank")


# user fields
userFields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String
}


# Create Users resource for the API with get and post methods
class Users(Resource):
    @marshal_with(userFields) # marshal the output to JSON
    def get(self):
        users = UserModel.query.all()
        return users

    def post(self):
        @marshal_with(userFields)
        args = user_args.parse_args()
        user = UserModel(name=args['name'], email=args['email'])
        db.session.add(user) # add user to session
        db.session.commit()
        users = UserModel.query.all()
        return users, 201 # return 201 status code - created


# another user
class User(Resource):
    @marshal_with(userFields)
    def get(self, user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if not user:
            abort(404, message="User not found")
        return user

    @marshal_with(userFields)
    def patch(self, id):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User not found")
        # update database
        user.name = args['name']
        user.email = args['email']
        # commit changes to db
        db.session.commit()
        return user

    @marshal_with(userFields)
    def delete(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User not found")
        # commit changes to db
        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 204

# assign Users Resource to url
api.add_resource(Users, '/api/users/')
api.add_resource(User, '/api/users/<int:id>')


# Create a new route for home page
@app.route('/')
def home():
    return '<h1>Flask REST API</h1>'


if __name__ == '__main__':
    app.run(debug=True)
