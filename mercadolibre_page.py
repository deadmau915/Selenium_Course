from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MercadoLibrePage(object):
    def __init__(self, driver):
        self._driver = driver
        self._url = 'https://mercadolibre.com/'

    def open(self):
        self._driver.get(self._url)

    def order_data(self, data):
        ordered_data = {}
        for element in data:
           ordered_data[element.text.lower()] = element
        return ordered_data

    def get_countries(self):
        countries = WebDriverWait(self._driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ml-site-link')))
        return self.order_data(countries)

    def select_country(self, country_name):
        countries = self.get_countries()
        countries[country_name.lower()].click()

    def search_product(self, keyword):
        search_field = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.NAME, 'as_word')))
        search_field.send_keys(keyword)
        search_field.submit()

    def accept_cookies(self):
        try:
            WebDriverWait(self._driver, 3).until(EC.presence_of_element_located((By.XPATH, '(//button[contains(@class, "cookie-consent-banner")])[1]'))).click()
        except:
            print("You already accepted the cookies in this website")

    def get_filters(self):
        filters_list = WebDriverWait(self._driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//li[@class="ui-search-filter-container shops__container-lists"]')))
        ordered_filters_list = {}
        for filter in filters_list:
            ordered_filters_list[filter.text.lower().split("\n")[0]] = filter
            print(filter.text.lower().split("\n")[0])
        return ordered_filters_list
    
    def set_filter(self, filter_name):
        mcl_filters = self.get_filters()
        mcl_filters[filter_name.lower()].click()

    def get_elements_in_sortfilter(self):
        WebDriverWait(self._driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'andes-dropdown__trigger'))).click()
        sortlist_items = self._driver.find_elements(By.XPATH,'//li[contains(@class, "andes-list__item")]')
        return self.order_data(sortlist_items)

    def sort_by(self, keyword):
        sortlist_items = self.get_elements_in_sortfilter()
        sortlist_items[keyword.lower()].click()

    def get_first_5_items(self):
        driver = self._driver
        WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//h2[@class="ui-search-item__title shops__item-title"]')))
        items_list = [[None, None]] * 5
        for i in range(5):
            items_list[i][0] = driver.find_element(By.XPATH, f'(//h2[@class="ui-search-item__title shops__item-title"])[{i+1}]').text
            items_list[i][1] = driver.find_element(By.XPATH, f'(//span[@class="price-tag-fraction"])[{2*i+1}]').text
        print(items_list)

    def search(self, search_text):
        search_field = self._driver.find_element(By.ID, 'cb1-edit')
        search_field.clear()
        search_field.send_keys(search_text)
        search_field.submit()