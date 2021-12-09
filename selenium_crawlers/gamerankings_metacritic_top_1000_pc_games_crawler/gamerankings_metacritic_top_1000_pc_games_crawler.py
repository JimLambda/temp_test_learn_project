import time
import imghdr

import requests
import xlsxwriter
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib3.exceptions import ConnectTimeoutError

total_page = 20

file_name = './result_data/game_data_{}.xlsx'.format(time.strftime('%Y%m%d%H%M%S'))

workbook = xlsxwriter.Workbook(filename=file_name)
worksheet = workbook.add_worksheet()

# options = webdriver.ChromeOptions()
# proxy = '127.0.0.1:10809'
# options.add_argument('--proxy-server=' + proxy)
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()

# driver.set_page_load_timeout(10)

page = 0
while page < total_page:
    try:
        driver.get("https://www.metacritic.com/browse/games/release-date/available/pc/metascore?page=" + str(page))
    except TimeoutException as e:
        print(e)
        continue

    title_element_list = driver.find_elements(By.CSS_SELECTOR, '.clamp-summary-wrap a.title h3')
    year_element_list = driver.find_elements(By.XPATH, value='//div[@class="clamp-details"]/span')
    meta_score_element_list = driver.find_elements(By.XPATH,
                                                   '//div[@class="clamp-score-wrap"]//div[@class="metascore_w large game positive"]')
    user_score_element_list = driver.find_elements(By.XPATH, '//div[@class="clamp-userscore"]/a/div')
    img_element_list = driver.find_elements(By.XPATH, '//td[@class="clamp-image-wrap"]/a/img')
    platform_element_list = driver.find_elements(By.XPATH, '//div[@class="platform"]/span[@class="data"]')
    summary_element_list = driver.find_elements(By.XPATH, '//td[@class="clamp-summary-wrap"]/div[@class="summary"]')
    title_number_element_list = driver.find_elements(By.XPATH,
                                                     '//td[@class="clamp-summary-wrap"]/span[@class="title numbered"]')

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
            title_number_str = title_number_element_list[index].get_attribute('innerHTML')
            title_number_str = title_number_str.strip('. \"\'\n\t')
            title_number_int = int(title_number_str)
            img_src = img_element_list[index].get_attribute('src')
            platform_str = platform_element_list[index].text
            platform_str = platform_str.strip(' \"\'\n\t')
            summary_str = summary_element_list[index].get_attribute('innerHTML')
            summary_str = summary_str.strip(' \"\'\n\t')


            def get_and_save_img():
                try:
                    # response = requests.get(url=img_src, proxies={'http': 'http://127.0.0.1:10809', 'https': 'https://127.0.0.1:10809'})
                    response = requests.get(url=img_src)
                    with open(file='./result_data/image_temp_folder/{}.jpg'.format(title_number_int),
                              mode='wb') as file:
                        file.write(response.content)
                except ConnectTimeoutError as e:
                    print(e)
                    get_and_save_img()


            get_and_save_img()

            print(user_score_element_list)
            print(title_str, date_year_str, meta_score_str, 'user_score:', user_score_str)

            worksheet.write(title_number_int, 0, title_number_str)
            try:
                if imghdr.what('./result_data/image_temp_folder/{}.jpg'.format(title_number_int)) == 'jpeg':
                    worksheet.insert_image(title_number_int, 1,
                                           './result_data/image_temp_folder/{}.jpg'.format(title_number_int))
            except Exception as e:
                print(e)
            worksheet.write(title_number_int, 2, title_str)
            worksheet.write(title_number_int, 3, date_str)
            worksheet.write(title_number_int, 4, year_str)
            worksheet.write(title_number_int, 5, meta_score_str)
            worksheet.write(title_number_int, 6, user_score_str)
            worksheet.write(title_number_int, 7, platform_str)
            worksheet.write(title_number_int, 8, summary_str)

            index += 1
        except Exception as e:
            print(e)
            break

    page += 1

workbook.close()
