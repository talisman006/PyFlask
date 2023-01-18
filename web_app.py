from flask import Flask, request
from db_connector import get_user, create_user, modify_user, delete_user
import os
import signal


app = Flask(__name__)

# Supported methods:
@app.route('/users/get_user_data/<user_id>', methods=['GET'])

def get_user_name(user_id):
    result = get_user(user_id)
    if result is None:
        print(f'--debugging: user with ID {user_id} not found')
        return f"<h1 id='error'>Error: no such user with ID {user_id}</h1>", 404
    else:
        print(f'--debugging: returning user name: {result["user_name"]}')
        return f"<h1 id='user'>{result['user_name']}</h1>", 200


@app.route('/stop_server', methods=['GET'])
def stop_server():
    try:
        os.kill(os.getpid(), signal.CTRL_C_EVENT)
    except Exception as e:
        print("ERROR: Cannot stop server normally:")
        print(e)
        return 'Problem stopping server'
    return 'Server stopped'


# if __name__ == '__main__':
app.run(host='127.0.0.1', debug=True, port=5001)

# connection.close()