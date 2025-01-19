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
trados_window = None
codec_of_the_window = 'gbk'
for window in windows_list:
    try:
        print(str(window.get_title().decode('gbk')))
        codec_of_the_window = 'gbk'
    except UnicodeDecodeError as e:
        print(e)
        print(str(window.get_title().decode('utf-8')))
        codec_of_the_window = 'utf-8'
    if 'Trados Studio - ' in str(window.get_title().decode(codec_of_the_window)):
        trados_window = window
        break
if trados_window is None:
    raise Exception('SDL Trados Studio is not opened.')

current_time = 0
while True:
    current_time += 1
    if current_time > copy_times:
        break
    if trados_window is not None:
        trados_window.activate()
        ahk.send('!{Insert}')
        ahk.send('^a')
        ahk.send('^c')

    sogou_input_textarea_element = driver.find_element(by=By.CSS_SELECTOR, value='#trans-input')
    sogou_input_textarea_element.click()
    sogou_input_textarea_element.send_keys(Keys.CONTROL, 'a')
    sogou_input_textarea_element.send_keys(Keys.CONTROL, 'v')
    sleep(1.2)
    copy_button_element = driver.find_element(by=By.CSS_SELECTOR, value='.btn-copy')
    copy_button_element.click()

    if trados_window is not None:
        trados_window.activate()
        ahk.send('^v')
        ahk.send('{Down}')
