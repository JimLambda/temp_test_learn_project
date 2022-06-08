from time import sleep

from selenium import webdriver
from ahk import AHK
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

copy_times = 10000

driver = webdriver.Chrome()

driver.get('https://fanyi.sogou.com/')

ahk = AHK()
windows_list = list(ahk.windows())
print(windows_list)
memoq_window = None
for window in windows_list:
    print(str(window.get_title().decode('gbk')))
    if str(window.get_title().decode('gbk')).startswith('memoQ - '):
        memoq_window = window
        break
if memoq_window is None:
    raise Exception('memoQ is not opened.')

current_time = 0
while True:
    current_time += 1
    if current_time > copy_times:
        break
    if memoq_window is not None:
        memoq_window.activate()
        ahk.send('^+s')
        sleep(1.2)
        ahk.send('^a')
        sleep(0.2)
        ahk.send('^c')

    button_clear_element = None
    try:
        button_clear_element = driver.find_element(by=By.CSS_SELECTOR, value='.trans-con>.btn-clear')
    except Exception as e:
        print(e)
        print("Clear text button not found.")
    try:
        button_clear_element.click()
    except Exception as e:
        print(e)
        print("Clear text button somehow cannot be clicked.")
    sleep(0.2)
    sogou_input_textarea_element = driver.find_element(by=By.CSS_SELECTOR, value='#trans-input')
    sogou_input_textarea_element.click()
    sogou_input_textarea_element.send_keys(Keys.CONTROL, 'a')
    sogou_input_textarea_element.send_keys(Keys.CONTROL, 'v')
    sleep(2.0)
    copy_button_element = driver.find_element(by=By.CSS_SELECTOR, value='.btn-copy')
    copy_button_element.click()

    if memoq_window is not None:
        memoq_window.activate()
        ahk.send('^v')
        ahk.send('{Down}')
