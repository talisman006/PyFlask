## This code works with db.connector flask server (not rest.app) ###

#### Backend testing ####

import requests
import time

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
    print('-- debug: response.text:', response.text)
    print('-- debug: response.json:', response.json)
    print('-- debug: response.status_code:', response.status_code)
    # pass

# Set the base URL for the API
BASE_URL = 'http://127.0.0.1:5000'


space()

print("POST METHOD TESTING - NON EXISTING USER:")
# Send a POST request to create a new user
response = requests.post(f'{BASE_URL}/users/3', json={'user_name': 'Emmett'})
debug(response)
# Check the response body from the API server and see if it's what we expect it to be or something else:
expect_response(response, {'user_added': 'Emmett', 'status': 'ok'})
# Check the status code respectively:
expect_status(response, 200)

time.sleep(2)
space()

print("GET METHOD TESTING FOR EXISTING USER:")
# Send a GET request to retrieve an existing user:
response = requests.get(f'{BASE_URL}/users/3')
debug(response)
# Check the response body from the API server and see if it's what we expect it to be or something else:
expect_response(response, {'user_id': 3, 'user_name': 'Emmett'})
# Check the status code respectively:
expect_status(response, 200)


space()


time.sleep(3)


#### Frontend Testing ####


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait



# Create a webdriver instance
driver = webdriver.Chrome(service=Service("D:\\Devops Course\Installations\chromedriver_win32\chromedriver.exe"))
driver.implicitly_wait(10) ### conditional synchronization


print("Test the get_user_name function with a valid user ID:")

driver.get("http://127.0.0.1:5001/users/get_user_data/3")
user_name_element = driver.find_element(By.ID, "user")

print('--debug: user_name_element.text is:', user_name_element.text)

try:
    if user_name_element.text == "Emmett":
        print(f"TEST PASSED SUCCESSFULLY for user with ID 3: User element found. User name is: {user_name_element.text}")
    else:
        raise Exception(f"Unexpected user name: {user_name_element.text}")
except Exception as e:
    print(f"TEST FAILED for user with ID 3: {e}")



space()


time.sleep(3)



# UTILITY: Send a DELETE request for the test user
response = requests.delete(f'{BASE_URL}/users/3')
# debug(response)
# Check the response body from the API server and see if it's what we expect it to be or something else:
# expect_response(response, {'user_id': '3', 'status': 'deleted'})
# Check the status code respectively:
# expect_status(response, 200)
print('UTILITY: Test user deleted')



driver.quit()