import time
import requests


def check_response(response, expected_status_code):
    try:
        if response.status_code != expected_status_code:
            raise Exception(f'Error stopping the server, expected status code {expected_status_code} but got {response.status_code} with error text: {response.text}')
    except Exception as e:
        print(f'Error message: {e} with status code: {response.status_code}')
    else:
        print(f'Server response: {response.text}')


print("-- Trying to stop server http://127.0.0.1:5000")
response = requests.get('http://127.0.0.1:5000/stop_server')
check_response(response, 200)

time.sleep(1)

print("-- Trying to stop server http://127.0.0.1:5001")
response = requests.get('http://127.0.0.1:5001/stop_server')
check_response(response, 200)
