import time
from colorama import Fore, Back, Style
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

print(Fore.RED + Back.BLUE + Style.BRIGHT + 'Encoding message with Base64...' +
      Style.RESET_ALL)
print(Fore.CYAN + 'Opening session...' + Style.RESET_ALL)
time.sleep(1)

options_cfg = Options()
options_cfg.add_argument('--headless')
options_cfg.add_argument('windows-size=500,500')

chrome_browser = webdriver.Chrome(options=options_cfg)
chrome_browser.get('https://www.base64encode.org')

#  looking for element
encode_button = chrome_browser.find_element(
    By.XPATH, "//button[text()='ENCODE']")

# Boolean output for finding element
# assert "ENCODE" in chrome_browser.page_source

user_message = chrome_browser.find_element(By.ID, "input")
user_message.clear()

print(Fore.CYAN + '[INFO] Writing message...' + Style.RESET_ALL)
user_message.send_keys('catch_curious.py  ;)')

encode_button.click()
print(Fore.CYAN + '[INFO] Encrypting...' + Style.RESET_ALL)
output_message = chrome_browser.find_element(By.ID, "output")

print(Style.BRIGHT + Fore.YELLOW +
      output_message.get_attribute('value') + Style.RESET_ALL)
print(Fore.CYAN + '[INFO] Encription done.' + Style.RESET_ALL)
chrome_browser.quit()
