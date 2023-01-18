import pymysql
from flask import Flask, request


def open_connection():
    return pymysql.connect(
        host='sql.freedb.tech',
        port=3306,
        user='freedb_Rikile',
        passwd='qm9N2*5a%qV6Sqc',
        db='freedb_Lesson5',
        cursorclass=pymysql.cursors.DictCursor)


def get_user(user_id):
    try:
        # Connect to the MySQL database
        with open_connection() as connection, connection.cursor() as cursor:
            # connection.autocommit(True)

            # Retrieve the user from the MySQL database
            sql = "SELECT `user_name`,`user_id` FROM freedb_Lesson5.users WHERE user_id=%s"
            cursor.execute(sql, (user_id,))
            result = cursor.fetchone()
            # print('--debug:', result)
            return {"user_id": user_id, "user_name": result["user_name"]}
    except Exception as e:
        print(e)
        return None


###########################

# POST return True on success
def create_user(user_id, user_name):
    try:
        # Connect to the MySQL database
        with open_connection() as connection, connection.cursor() as cursor:
            # connection.autocommit(True)

            sql = 'INSERT INTO users (user_id, user_name, creation_date) VALUES (%s, %s, NOW())'
            cursor.execute(sql, (user_id, user_name,))
            connection.commit()
            # upon success:
            return True
    except Exception as e:
        print(e)
        return False


###########################

# PUT return True on success
def modify_user(user_id, new_user_name):
    try:
        # Connect to the MySQL database
        with open_connection() as connection, connection.cursor() as cursor:
            # connection.autocommit(True)

            # check if user already exists
            sql = 'SELECT * FROM users WHERE user_id=%s'
            cursor.execute(sql, (user_id))
            result = cursor.fetchone()
            if result is None:
                return False

            # update the user name in the MySQL database
            sql = 'UPDATE users SET user_name=%s WHERE user_id=%s'
            cursor.execute(sql, (new_user_name, user_id))
            connection.commit()
            # return a message to confirm that the user name was updated
            return True
    except Exception as e:
        print(e)
        return False


def delete_user(user_id):
    try:
        with open_connection() as connection, connection.cursor() as cursor:
            # Retrieve the user from the MySQL database
            sql = 'SELECT * FROM users WHERE user_id=%s'
            cursor.execute(sql, (user_id,))
            result = cursor.fetchone()
            if result is None:  # if user doesn't exist
                return False

            # delete the user from the MySQL database
            sql = 'DELETE FROM users WHERE user_id=%s'
            cursor.execute(sql, (user_id,))
            connection.commit()
            # return a message to confirm that the user was deleted
            return True
    except Exception as e:
        print(e)
        return False


