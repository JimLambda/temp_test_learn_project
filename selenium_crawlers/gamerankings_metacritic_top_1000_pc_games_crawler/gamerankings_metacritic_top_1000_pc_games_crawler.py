import time

from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By

total_page = 20

file_name = 'game_data_{}.csv'.format(time.strftime('%Y%m%d%H%M%S'))

options = webdriver.ChromeOptions()
proxy = '127.0.0.1:10809'
options.add_argument('--proxy-server=' + proxy)
driver = webdriver.Chrome(options=options)

driver.set_page_load_timeout(10)

page = 0
while page <= total_page:
    try:
        driver.get("https://www.metacritic.com/browse/games/release-date/available/pc/metascore?page=" + str(page))
    except TimeoutException as e:
        print(e)

    title_element_list = driver.find_elements(By.CSS_SELECTOR, '.clamp-summary-wrap a.title h3')
    year_element_list = driver.find_elements(By.XPATH, value='//div[@class="clamp-details"]/span')
    meta_score_element_list = driver.find_elements(By.XPATH,
                                                   '//div[@class="clamp-score-wrap"]//div[@class="metascore_w large game positive"]')
    user_score_element_list = driver.find_elements(By.XPATH, '//div[@class="clamp-userscore"]/a/div')

    if len(title_element_list) == 0:
        continue

    index = 0
    while True:
        try:
            title_str = title_element_list[index].text
            date_year_str = year_element_list[index].text
            date_year_temp_list = date_year_str.split(', ')
            date_str = date_year_temp_list[0]
            year_str = date_year_temp_list[1]
            meta_score_str = meta_score_element_list[index].text
            user_score_str = user_score_element_list[index].get_attribute('innerHTML')
            print(user_score_element_list)
            print(title_str, date_year_str, meta_score_str, 'user_score:', user_score_str)
            with open(file=file_name, mode='a') as file:
                file.write(
                    title_str + ',' + date_str + ',' + year_str + ',' + meta_score_str + ',' + user_score_str + '\n')
            index += 1
        except Exception as e:
            print(e)
            break

    page += 1
