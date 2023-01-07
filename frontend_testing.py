import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# Create a webdriver instance
driver = webdriver.Chrome(service=Service("D:\\Devops Course\Installations\chromedriver_win32\chromedriver.exe"))
driver.implicitly_wait(10) ### conditional synchronization


print("Test the get_user_name function with a valid user ID:")

driver.get("http://127.0.0.1:5001/users/get_user_data/10")
user_name_element = driver.find_element(By.ID, "user")

print('--debug: user_name_element.text is:', user_name_element.text)

try:
    if user_name_element.text == "Lucy":
        print(f"TEST PASSED SUCCESSFULLY for user with ID 10: User element found. User name is: {user_name_element.text}")
    else:
        raise Exception(f"Unexpected user name: {user_name_element.text}")
except Exception as e:
    print(f"TEST FAILED for user with ID 10: {e}")


time.sleep(2)

print("Test the get_user_name function with an invalid user ID:")

driver.get(f"http://127.0.0.1:5001/users/get_user_data/600")
error_element = driver.find_element(By.ID, "error")
print('--debug: error_element =', error_element.text)
try:
    if error_element.text == f"Error: no such user with ID 600":
        print(f"TEST PASSED SUCCESSFULLY for user with ID 600: User not found")
except Exception as e:
    print(f"TEST FAILED for user with ID 600: {e}")

time.sleep(2)


# Close the webdriver instance
driver.quit()