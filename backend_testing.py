## This code works with db.connector flask server ###

import requests

# A function that compares the response from the API server with what we expect to receive in each test:
def expect_response(response, expected):
    # try:
        if response.json() == expected:
            print('TEST PASSED SUCCESSFULLY - response is as expected')
        else:
            print('TEST FAILED: We expected response:')
            print(expected)
            print('We got response:')
            print(response.text)
    # except Exception:
    #     print('ERROR: response not in JSON:')
    #     print(response.text)

def expect_status(response, expected_status):
    try:
        if response.status_code == expected_status:
            print('TEST PASSED SUCCESSFULLY - status code is as expected')
        else:
            print('TEST FAILED: We expected status code:')
            print(expected_status)
            print('We got status code:')
            print(response.status_code)
    except Exception:
        print('ERROR: status response not in JSON:')
        print(response.status_code)

def space():
    print(' ')
    print('----------------------------------')
    print(' ')

def debug(response):
    # print('-- debug: response.text:', response.text)
    # print('-- debug: response.json:', response.json)
    # print('-- debug: response.status_code:', response.status_code)
    pass

# Set the base URL for the API
BASE_URL = 'http://127.0.0.1:5000'


space()

print("POST METHOD TESTING - NON EXISTING USER:")
# Send a POST request to create a new user
response = requests.post(f'{BASE_URL}/users/1', json={'user_name': 'Alice'})
debug(response)
# Check the response body from the API server and see if it's what we expect it to be or something else:
expect_response(response, {'user_added': 'Alice', 'status': 'ok'})
# Check the status code respectively:
expect_status(response, 200)


space()

print("POST METHOD TESTING - EXISTING USER:")
# Send a POST request to create a new user on an existing ID:
response = requests.post(f'{BASE_URL}/users/1', json={'user_name': 'Bob'})
debug(response)
# Check the response body from the API server and see if it's what we expect it to be or something else:
expect_response(response, {"reason": "id already exists", "status": "error"})
# Check the status code respectively:
expect_status(response, 400)


space()

print("GET METHOD TESTING FOR EXISTING USER:")
# Send a GET request to retrieve an existing user:
response = requests.get(f'{BASE_URL}/users/1')
debug(response)
# Check the response body from the API server and see if it's what we expect it to be or something else:
expect_response(response, {'user_id': 1, 'user_name': 'Alice'})
# Check the status code respectively:
expect_status(response, 200)


space()

print("GET METHOD TESTING FOR NON-EXISTING USER:")
# Send a GET request to retrieve an existing user:
response = requests.get(f'{BASE_URL}/users/5842')
debug(response)
# Check the response body from the API server and see if it's what we expect it to be or something else:
expect_response(response, {'error': f'User with id 5842 does not exist'})
# Check the status code respectively:
expect_status(response, 404)


space()

print("PUT METHOD TESTING - EXISTING USER:")
# Send a PUT request trying to update new data for existing user ID:
response = requests.put(f'{BASE_URL}/users/1', json={'user_name': 'Charley'})
debug(response)
# Check the response body from the API server and see if it's what we expect it to be or something else:
expect_response(response, {'user_id': '1', 'user_name': 'Charley', 'status': 'updated'})
# Check the status code respectively:
expect_status(response, 200)


space()

print("PUT METHOD TESTING - NON-EXISTING USER:")
# Send a PUT request trying to update new data for non-existing user ID:
response = requests.put(f'{BASE_URL}/users/938', json={'user_name': 'David'})
debug(response)
# Check the response body from the API server and see if it's what we expect it to be or something else:
expect_response(response, {'error': f'User with id 938 does not exist'})
# Check the status code respectively:
expect_status(response, 404)


space()

print("DELETE METHOD TESTING: EXISTING USER")
# Send a DELETE request to delete the user
response = requests.delete(f'{BASE_URL}/users/1')
debug(response)
# Check the response body from the API server and see if it's what we expect it to be or something else:
expect_response(response, {'user_id': '1', 'status': 'deleted'})
# Check the status code respectively:
expect_status(response, 200)


space()
print("DELETE METHOD TESTING: NON-EXISTING USER")
# Send a DELETE request to delete the user
response = requests.delete(f'{BASE_URL}/users/543')
debug(response)
# Check the response body from the API server and see if it's what we expect it to be or something else:
expect_response(response, {'error': f'User with id 543 does not exist or invalid request'})
# Check the status code respectively:
expect_status(response, 404)


space()