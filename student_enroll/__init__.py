import markdown
import os
import shelve

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("students.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    """Present some documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)


class studentList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        students = []

        for key in keys:
            students.append(shelf[key])

        return {'message': 'Success', 'data': students}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('roll_number', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('stream', required=True)

        # Parse the arguments into an object
        args = parser.parse_args()

        shelf = get_db()
        shelf[args['roll_number']] = args

        return {'message': 'student enrolled', 'data': args}, 201


class student(Resource):
    def get(self, roll_number):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (roll_number in shelf):
            return {'message': 'student record not found', 'data': {}}, 404

        return {'message': 'student record found', 'data': shelf[roll_number]}, 200

    def delete(self, roll_number):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (roll_number in shelf):
            return {'message': 'student not found', 'data': {}}, 404

        del shelf[roll_number]
        return '', 204


api.add_resource(studentList, '/students')
api.add_resource(student, '/student/<string:roll_number>')



