from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

all_companies_that_can_deal_with_foreign_languages_page_1_url = "https://suumo.jp/jj/fudousan/ichiran/FR351FC001/?ar=030&bs=041&ta=13&sc=13101&sc=13102&sc=13103&sc=13104&sc=13105&sc=13113&sc=13106&sc=13107&sc=13108&sc=13118&sc=13121&sc=13122&sc=13123&sc=13109&sc=13110&sc=13111&sc=13112&sc=13114&sc=13115&sc=13120&sc=13116&sc=13117&sc=13119&sc=13201&sc=13202&sc=13203&sc=13204&sc=13205&sc=13206&sc=13207&sc=13208&sc=13209&sc=13210&sc=13211&sc=13212&sc=13213&sc=13214&sc=13215&sc=13218&sc=13219&sc=13220&sc=13221&sc=13222&sc=13223&sc=13224&sc=13225&sc=13227&sc=13228&sc=13229&sc=13300&stf=401&pc=100&po=02&pj=2"
all_houses_page_1_url = "https://suumo.jp/jj/chintai/ichiran/FR301FC005/?ar=030&bs=040&ta=13&sc=13101&sc=13102&sc=13103&sc=13104&sc=13105&sc=13113&sc=13106&sc=13107&sc=13108&sc=13118&sc=13121&sc=13122&sc=13123&sc=13109&sc=13110&sc=13111&sc=13112&sc=13114&sc=13115&sc=13120&sc=13116&sc=13117&sc=13119&cb=0.0&ct=6.0&mb=20&mt=9999999&et=5&cn=9999999&tc=0400101&tc=0400501&tc=0400301&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sngz=&po1=00&po2=99&pc=100"

if __name__ == '__main__':
    driver.get(all_companies_that_can_deal_with_foreign_languages_page_1_url)
    with open(file="./list_of_all_companies_that_can_deal_with_foreign_languages.txt", mode="w", encoding="utf-8",
              newline="\n") as file:
        while True:
            all_title_elements_on_this_page = driver.find_elements(by=By.XPATH,
                                                                   value="//h2[@class='listtitleunit-title']/a[@class='js-cassetLinkHref']")
            title_text_list = []
            for title_element in all_title_elements_on_this_page:
                title_text = title_element.text
                title_text_list.append(title_text + "\n")
            file.writelines(title_text_list)
            next_page_elements = driver.find_elements(by=By.XPATH,
                                                      value='//div[@class="pagination pagination_set-nav"]/p/a[text()="次へ"]')
            if len(next_page_elements) == 0:
                break
            else:
                next_page_elements[0].click()
            sleep(1)

    names_of_all_companies_which_deal_foreign_languages = []
    with open(file="./list_of_all_companies_that_can_deal_with_foreign_languages.txt", mode="r", encoding="utf-8",
              newline="\n") as file:
        names_of_all_companies_which_deal_foreign_languages.extend(file.readlines())
        for list_index, company_name in enumerate(names_of_all_companies_which_deal_foreign_languages):
            new_company_name = company_name.strip()
            names_of_all_companies_which_deal_foreign_languages[list_index] = new_company_name

    driver.get(all_houses_page_1_url)
    with open(file="./found_houses.csv", mode="w", encoding="utf-8",
              newline="\n") as file:
        while True:
            all_house_elements_in_this_page = driver.find_elements(by=By.XPATH,
                                                                   value="//div[contains(concat(' ', normalize-space(@class), ' '), ' property ')]")
            for house_element in all_house_elements_in_this_page:

                company_element = house_element.find_element(by=By.XPATH,
                                                             value='./descendant::div[@class="detailnote-box-item"]/div[1]')

                company_name = ""
                try_to_find_company_name_elements = company_element.find_elements(by=By.XPATH, value='./child::a')
                if len(try_to_find_company_name_elements) > 0:
                    company_name_element = company_element.find_element(by=By.XPATH, value='./child::a')
                    company_name = company_name_element.text
                else:
                    company_name = company_element.text

                for name_of_company_that_can_deal_with_foreign_languages in names_of_all_companies_which_deal_foreign_languages:
                    if company_name.strip() == name_of_company_that_can_deal_with_foreign_languages.strip():
                        house_name_element = house_element.find_element(by=By.XPATH,
                                                                        value='./descendant::a[@class="js-cassetLinkHref"]')
                        house_price_element = house_element.find_element(by=By.XPATH,
                                                                         value='./descendant::div[@class="detailbox-property-point"]')
                        house_name = house_name_element.text
                        house_price = house_price_element.text
                        file.write(house_name + "," + house_price + "," + company_name + "\n")
                        break

            next_page_elements = driver.find_elements(by=By.XPATH,
                                                      value='//div[@class="pagination pagination_set-nav"]/p/a[text()="次へ"]')
            if len(next_page_elements) == 0:
                break
            else:
                next_page_elements[0].click()
            sleep(1)

    driver.close()
