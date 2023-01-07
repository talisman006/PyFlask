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
    @app.route('/users/get_user_data/<user_id>', methods=['GET'])

    def get_user_name(user_id):
        try:
            print(f'--debugging: received request for user ID {user_id}')
            # Retrieve the user from the MySQL database
            with connection.cursor() as cursor:
                sql = "SELECT `user_name`,`user_id` FROM freedb_Lesson5.users WHERE user_id=%s"
                cursor.execute(sql, (user_id,))
                result = cursor.fetchone()
                print(f"--debugging: query result = {result}") # Print the value of the result variable
        except Exception as e:
            print(f'Error: {e}')
            return {'error': str(e)}, 500
        if result is None:
            print(f'--debugging: user with ID {user_id} not found')
            return f"<h1 id='error'>Error: no such user with ID {user_id}</h1>", 404
        else:
            print(f'--debugging: returning user name: {result["user_name"]}')
            return f"<h1 id='user'>{result['user_name']}</h1>", 200



except Exception as e:
    handle_error(e)



if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5001)

# connection.close()