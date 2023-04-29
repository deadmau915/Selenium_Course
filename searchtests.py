import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class SearchTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://madison-island.com/')
    
    def test_search_tee(self):
        driver = self.driver
        #the input field is not able to interact unless we click the "search button", so
        #We find the element who is taking the click, in this case is the form which contains the input and the button element
        #There is 2 same exact 'form' elements in the DOM, one for desktop, another one for mobile, thats why We take the xpath,
        #to select just the one We want work with
        click_to_able_search_field = driver.find_element(By.XPATH, "(//form[@action='/search'])[2]")
        click_to_able_search_field.click()
        #once We click the "search button", the input search field is able to interact
        search_field = driver.find_element(By.XPATH, "(//input[@name='q'])[2]")
        search_field.send_keys('tee')
        search_field.submit()
    
    def test_search_salt_shaker(self):
        driver = self.driver
        click_to_able_search_field = driver.find_element(By.XPATH, '(//form[@action="/search"])[2]')
        click_to_able_search_field.click()
        search_field = driver.find_element(By.XPATH, "(//input[@name='q'])[2]")
        search_field.send_keys('salt shaker')
        search_field.submit()
        products = driver.find_elements(By.XPATH, "//a[contains(@href, 'shaker')]")
        self.assertEqual(1, len(products))

    def tearDown(self):
        self.driver.quit()