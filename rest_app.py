from flask import Flask, request

app = Flask(__name__)

# local users dictionary storage
users = {}

# General exception handler function
def handle_error(e):
    return {'error': str(e)}, 500

# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):

    try:


        if request.method == 'GET':
            # attempt to retrieve the value stored in the users dictionary under the key user_id.
            try:
                user_name = users[user_id]
            except KeyError:
                return {'error': f'User with id {user_id} does not exist'}, 404
            except TypeError:
                return {'error': 'User ID is missing or invalid'}, 400
            else:
                return {'user_id': user_id, 'user_name': user_name}, 200  # status code



        elif request.method == 'POST':
            # getting the json data payload from request
            try:
                # try to get request data
                request_data = request.json
            except Exception:
                # handle exception if request data is invalid
                return {'error': 'Invalid request data'}, 400
            # treating request_data as a dictionary to get a specific value from key
            try:
                # try to get user_name from request data
                user_name = request_data['user_name']
            except KeyError:
                # handle exception if user_name is missing from request data
                return {'error': 'Missing user_name in request data'}, 400
            # check if user ID already exists
            if user_id in users:
                return {'error': 'User ID already exists'}, 400
            # store the user_name value in the users dictionary under the key user_id:
            users[user_id] = user_name
            return {'user_id': user_id, 'user_name': user_name, 'status': 'saved'}, 200  # status code



        elif request.method == 'PUT':
            # check if user already exists
            try:
                user_name = users[user_id]
            except KeyError:
                return {'error': f'User with id {user_id} does not exist'}, 404
            # get the new user name from the request data
            try:
                new_user_name = request.json['user_name']
            except (KeyError, TypeError):
                return {'error': 'Missing user_name in request data'}, 400
            # update the user name in the users dictionary
            users[user_id] = new_user_name
            # return a message to confirm that the user name was updated
            return {'user_id': user_id, 'user_name': new_user_name, 'status': 'updated'}, 200



        elif request.method == 'DELETE':
            try:
                # delete the user from the users dictionary
                del users[user_id]
            except KeyError:
                return {'error': f'User with id {user_id} does not exist'}, 404
            except TypeError:
                return {'error': 'User ID is missing or invalid'}, 400
            # return a message to confirm that the user was deleted
            return {'user_id': user_id, 'status': 'deleted'}, 200

    except Exception as e:
        return handle_error(e)


app.run(host='127.0.0.1', debug=True, port=5000)