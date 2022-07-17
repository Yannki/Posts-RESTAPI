# main.py
from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields
import requests
import json

#######################Settings############################

flask_app = Flask(__name__)
app = Api(app=flask_app,
          version="1.0",
          title="Post Manager",
          description="Manage posts associated to users from external API")

name_space = app.namespace("", description='User posts API')
###########################################################

#####################External API Data#####################
posts_api = requests.get('https://jsonplaceholder.typicode.com/posts')
posts_data = posts_api.text
external_posts = json.loads(posts_data)

users_api = requests.get('https://jsonplaceholder.typicode.com/users')
users_data = users_api.text
users = json.loads(users_data)
############################################################

###################Local Mock Data##########################
posts = [{
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
},
    {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
}]
############################################################

########################Models##############################
post_model = app.model('Post',
                       {'id': fields.Integer,
                        'userId': fields.Integer,
                        'title': fields.String,
                        'body': fields.String})
############################################################

####################Adding a post###########################


@name_space.route("/posts")
class PostsCreateResource(Resource):

    @app.expect(post_model)
    @app.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    def post(self):
        try:
            data = request.get_json()
            for i in range(0, users):
                if users[i]['id'] == data['userId']:
                    for j in range(0, posts):
                        if users[i]['id'] == data['userId'] and posts[j]['id'] == data['id']:
                            name_space.abort(
                                500, e.__doc__, status="Could not retrieve information", statusCode="400")
                    posts.append(data)
                    return jsonify(posts)

        except Exception as e:
            name_space.abort(
                400, e.__doc__, status="Could not retrieve information", statusCode="400")

######Getting, updating and deleting a post by post id######


@name_space.route("/posts<int:id>")
class PostsResource(Resource):
    @app.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'id': 'Specify the Id associated with the person'})
    def get(self, id):
        try:
            for i in range(0, len(posts)):
                if posts[i]['id'] == id:
                    return jsonify(posts[i])

            for i in range(0, len(external_posts)):
                if external_posts[i]['id'] == id:
                    return jsonify(external_posts[i])

            name_space.abort(
                500, e.__doc__, status="Could not retrieve information", statusCode="500")

        except Exception as e:
            name_space.abort(
                400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @app.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'id': 'Specify the Id associated with the person'})
    def put(self, id):
        try:
            pass

            name_space.abort(
                500, e.__doc__, status="Could not retrieve information", statusCode="500")

        except Exception as e:
            name_space.abort(
                400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @app.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'id': 'Specify the Id associated with the person'})
    def delete(self, id):
        try:
            for i in range(0, len(posts)):
                if posts[i]['id'] == id:
                    return jsonify(posts.pop(i))

            name_space.abort(
                500, e.__doc__, status="Could not retrieve information", statusCode="500")

        except Exception as e:
            name_space.abort(
                400, e.__doc__, status="Could not retrieve information", statusCode="400")

####################Getting posts by userId#######################


@name_space.route("/posts/users<int:id>")
class UsersResouces(Resource):

    @app.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'id': 'Specify the Id associated with the person'})
    def get(self, id):
        users_posts = []
        try:
            for i in range(0, len(users)):
                if users[i]['id'] == id:
                    for i in range(0, len(posts)):
                        if posts[i]['userId'] == id:
                            user_posts.append(posts[i])
                    return jsonify(user_posts)

            name_space.abort(
                500, e.__doc__, status="Could not retrieve information", statusCode="500")

        except Exception as e:
            name_space.abort(
                400, e.__doc__, status="Could not retrieve information", statusCode="400")
