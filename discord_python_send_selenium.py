from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.edge.service import Service as EdgeService
import random

def type_message(element, message):
    for char in message:
        sleep_time = random.uniform(0.06, 0.08)  # random sleep to simulate human typing, adjust as you like
        time.sleep(sleep_time)
        element.send_keys(char)


def login_and_send_message(username, password, server_name, channel_name, message):
    # Setup WebDriver
    s = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=s)
    wait = WebDriverWait(driver, 20)

    # Navigate to Discord login page
    driver.get("https://discord.com/login")

    # Enter login information
    wait.until(EC.element_to_be_clickable((By.NAME, 'email'))).send_keys(username)
    wait.until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys(password + Keys.RETURN)

    # Allow time for login
    time.sleep(2)

    # Select server
    server_elem = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@data-dnd-name='{server_name}']")))
    server_elem.click()

    time.sleep(1)
    

    # Type message
    message_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='textbox']")))


    type_message(message_box, message + Keys.RETURN)

    # Cleanup WebDriver
    time.sleep(1)  # Allow time for message to send
    driver.quit()

# Replace with your actual details



def main():
    print("Starting...")
   
    login_and_send_message('your_email@exsample.com', 'your_password', 'your_server_name', 'ignore_this', 'your_message')

if __name__ == "__main__":
    main()