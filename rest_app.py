from flask import Flask, request
from db_connector import get_user, create_user, modify_user, delete_user

app = Flask(__name__)


# Supported methods:
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        result = get_user(user_id)
        if result is None:
            return {'error': f'User with id {user_id} does not exist'}, 404  # status code
        else:
            return {'user_id': result['user_id'], 'user_name': result['user_name']}, 200  # status code


    elif request.method == 'POST':
        # getting the json data payload from request
        try:
            # try to get request data
            request_data = request.json
        except Exception:
            # handle exception if request data is invalid
            return {'error': 'Invalid request data'}, 400
        try:
            # try to get user_name from request data
            user_name = request_data['user_name']
        except KeyError:
            # handle exception if user_name is missing from request data
            return {'error': 'Missing user_name in request data'}, 400
        # try to insert the new user into the MySQL database
        success = create_user(user_id, user_name)
        if success:
            return {'user_added': user_name, 'status': 'ok'}, 200  # status code
        else:
            return {'status': 'error', 'reason': 'id already exists'}, 400


    elif request.method == 'PUT':

        # get the new user name from the request data
        try:
            new_user_name = request.json['user_name']
        except (KeyError, TypeError):
            return {'error': 'Missing user_name in request data'}, 400
        # update the user name in the MySQL database
        success = modify_user(user_id, new_user_name)
        if success:
            # return a message to confirm that the user name was updated
            return {'user_id': user_id, 'user_name': new_user_name, 'status': 'updated'}, 200
        else:
            return {'error': f'User with id {user_id} does not exist'}, 404


    elif request.method == 'DELETE':
        success = delete_user(user_id)
        if success:
            return {'user_id': user_id, 'status': 'deleted'}, 200
        else:
            return {'error': f'User with id {user_id} does not exist or invalid request'}, 404


@app.route('/stop_server', methods=['GET'])
def stop_server():
    try:
        os.kill(os.getpid(), signal.CTRL_C_EVENT)
    except Exception as e:
        print("ERROR: Cannot stop server normally:")
        print(e)
        return 'Problem stopping server'
    return 'Server stopped'



if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000)

# connection.close()