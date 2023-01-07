import pymysql
from flask import Flask, request

app = Flask(__name__)

# General error handling func:
def handle_error(e):
    return {'error': str(e)}, 500

try:
    # Connect to the MySQL database
    connection = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_Rikile', passwd='qm9N2*5a%qV6Sqc',
                                       db='freedb_Lesson5', cursorclass=pymysql.cursors.DictCursor)
# connection.autocommit(True)
except Exception as e:
    handle_error(e)

try:

    # Supported methods:
    @app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])

    def user(user_id):


        if request.method == 'GET':

            # Retrieve the user from the MySQL database
            with connection.cursor() as cursor:
                sql = "SELECT `user_name`,`user_id` FROM freedb_Lesson5.users WHERE user_id=%s"
                cursor.execute(sql, (user_id,))
                result = cursor.fetchone()

            if result is None:
                return {'error': f'User with id {user_id} does not exist'}, 404 # status code
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
            try:
                with connection.cursor() as cursor:
                    sql = 'INSERT INTO users (user_id, user_name, creation_date) VALUES (%s, %s, NOW())'
                    cursor.execute(sql, (user_id, user_name,))
                    connection.commit()
            except Exception:
                return {'status': 'error', 'reason': 'id already exists'}, 400
            # upon success:
            return {'user_added': user_name, 'status': 'ok'}, 200  # status code


        elif request.method == 'PUT':
            # check if user already exists
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM users WHERE user_id=%s'
                cursor.execute(sql, (user_id))
                result = cursor.fetchone()
            if result is None:
                return {'error': f'User with id {user_id} does not exist'}, 404
            # get the new user name from the request data
            try:
                new_user_name = request.json['user_name']
            except (KeyError, TypeError):
                return {'error': 'Missing user_name in request data'}, 400
            # update the user name in the MySQL database
            with connection.cursor() as cursor:
                sql = 'UPDATE users SET user_name=%s WHERE user_id=%s'
                cursor.execute(sql, (new_user_name, user_id))
                connection.commit()
            # return a message to confirm that the user name was updated
            return {'user_id': user_id, 'user_name': new_user_name, 'status': 'updated'}, 200


        elif request.method == 'DELETE':
            # Retrieve the user from the MySQL database
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM users WHERE user_id=%s'
                cursor.execute(sql, (user_id,))
                result = cursor.fetchone()
            if result is None:
                return {'error': f'User with id {user_id} does not exist or invalid request'}, 404
            # delete the user from the MySQL database
            with connection.cursor() as cursor:
                sql = 'DELETE FROM users WHERE user_id=%s'
                cursor.execute(sql, (user_id,))
                connection.commit()
            # return a message to confirm that the user was deleted
            return {'user_id': user_id, 'status': 'deleted'}, 200

except Exception as e:
    handle_error(e)



if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000)

# connection.close()