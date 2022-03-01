from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_browser = webdriver.Chrome('./chromedriver.exe')

chrome_browser.maximize_window()
chrome_browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
assert "Selenium Easy Demo" in chrome_browser.title

print(chrome_browser.title)

close_dialog = chrome_browser.find_element(By.CLASS_NAME, "at4-close")
print(close_dialog.get_attribute('id'))
chrome_browser.implicitly_wait(20)
close_dialog.click()

show_message_button = chrome_browser.find_element(By.CLASS_NAME, "btn-default")
print(show_message_button.get_attribute("innerHTML"))

user_message = chrome_browser.find_element(By.ID, "user-message")
user_message.clear()
user_message.send_keys('EXTRA COOL hour is here')

show_message_button.click()

output_message = chrome_browser.find_element(By.ID, "display")

print(output_message.text)
assert 'EXTRA COOL hour is here' in output_message.text

chrome_browser.close()