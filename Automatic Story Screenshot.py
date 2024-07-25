from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your WebDriver (update as needed)
driver_path = '/path/to/chromedriver'

# Instagram login credentials
username = 'your_username'
password = 'your_password'

# Initialize the WebDriver
driver = webdriver.Chrome(executable_path=driver_path)

# Open Instagram login page
driver.get('https://www.instagram.com/accounts/login/')

# Wait for the login page to load
time.sleep(3)

# Log in to Instagram
driver.find_element(By.NAME, 'username').send_keys(username)
driver.find_element(By.NAME, 'password').send_keys(password)
driver.find_element(By.NAME, 'password').send_keys(Keys.RETURN)

# Wait for the login process to complete
time.sleep(5)

# Navigate to the user's story page
user_story_url = 'https://www.instagram.com/stories/username/'  # Replace 'username' with the actual username
driver.get(user_story_url)

# Wait for the story to load
time.sleep(5)

# Take a screenshot of the story
screenshot_path = 'instagram_story.png'
driver.save_screenshot(screenshot_path)

# Close the WebDriver
driver.quit()

print(f'Screenshot saved to {screenshot_path}')
