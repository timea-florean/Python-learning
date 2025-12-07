import os
import shutil
# Creating a backup of a file
source_file = 'example.txt'
backup_file = 'example_backup.txt'
shutil.copy(source_file, backup_file)
print(f"Backup of {source_file} created as {backup_file}.")
# Automatically organizing files by extension
for file in os.listdir('.'):
    if file.endswith('.txt'):
        if not os.path.exists('TextFiles'):
            os.mkdir('TextFiles')
            shutil.move(file, 'TextFiles')
            print(f"Moved {file} to TextFiles directory.")

#example of Web Automation Using Selenium:
from selenium import webdriver
# Setting up the WebDriver
driver = webdriver.Chrome()
# Opening a webpage
driver.get('https://example.com')
# Finding an element and interacting with it
input_element = driver.find_element_by_name('q')
input_element.send_keys('Python Automation')
input_element.submit()
# Closing the browser
driver.quit()

#example of using PyAutoGUI
import pyautogui
# Display the screen resolution
screen_width, screen_height = pyautogui.size()
print(f"Screen size: {screen_width}x{screen_height}")
# Move the mouse
pyautogui.moveTo(100, 150)
# Click the mouse
pyautogui.click()
# Write out a string
pyautogui.write('Hello, PyAutoGUI!', interval=0.25)
# Press the Enter key
pyautogui.press('enter')