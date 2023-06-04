from time import sleep

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def get_all_room_info():
    with open(file="./result.csv", mode="w", encoding="shiftjis", newline="\n") as file:
        file.write("物件名,賃料,管理費\n")
        for page_number in range(1, 99999):
            page_url = "https://www.citymobile.co.jp/recommend2/page/{}/?dsp%5Bexists%5D=1&dsp%5Blimit%5D=50".format(
                page_number)
            driver.get(page_url)

            all_buildings_elements_on_this_page = driver.find_elements(by=By.XPATH, value='//dd[@class="srcRes"]/ul/li')
            if len(all_buildings_elements_on_this_page) == 0:
                driver.close()
                return
            for li_element in all_buildings_elements_on_this_page:
                title_for_clicking = li_element.find_element(by=By.XPATH, value='.//div[@class="bukkenName"]/a')
                title_for_clicking.click()

                empty_house_title = driver.find_element(by=By.XPATH,
                                                        value='//dt[@class="article-list-title" and contains(text(), "【空室")]')
                parent_element = empty_house_title.find_element(by=By.XPATH, value='./..')

                # If there is "more" button, click it.
                # (If the building has more than 10 empty rooms, there will be a more button.)
                try:
                    more_button = parent_element.find_element(by=By.XPATH,
                                                              value='.//a[contains(@class, "btnListMore")]')
                    more_button.click()
                except selenium.common.exceptions.NoSuchElementException:
                    pass

                rent_fee_elements_list = parent_element.find_elements(by=By.XPATH, value='.//div[@class="rentFee"]')
                if len(rent_fee_elements_list) == 0:
                    driver.back()
                    continue
                manage_fee_elements_list = parent_element.find_elements(by=By.XPATH, value='.//div[@class="manageFee"]')
                building_name_element = driver.find_element(by=By.XPATH, value='//h2[@class="article-name"]')

                for index in range(0, len(rent_fee_elements_list)):
                    room_info_list = [building_name_element.text, rent_fee_elements_list[index].text,
                                      manage_fee_elements_list[index].text]
                    for room_info_list_index in range(1, 3):
                        room_info_list[room_info_list_index] = room_info_list[room_info_list_index].replace("円",
                                                                                                            "").replace(
                            ",",
                            "").strip()
                    file.write("{},{},{}\n".format(room_info_list[0], room_info_list[1], room_info_list[2]))
                    file.flush()

                driver.back()

        driver.close()


if __name__ == '__main__':
    get_all_room_info()
