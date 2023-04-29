import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner

class HomePagetest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.get('https://madison-island.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)
    
    def test_search_text_field(self):
        self.driver.find_element(By.XPATH, "//*[@id='shopify-section-header']/div/header/div/div[2]/div/div/form/input")
    
    def test_search_text_field_by_name(self):
        self.driver.find_element(By.NAME , "q")

    #find an element by his CLASS_NAME is buggy as I read it on stackover flow
    def test_search_text_field_by_class(self):
        self.driver.find_element(By.CLASS_NAME, "search-header__input search__input")

    def test_search_button_enabled(self):
        self.driver.find_element(By.XPATH, "//*[@id='shopify-section-header']/div/header/div/div[2]/div/div/form/button")

    def test_search_banner_img(self):
        banner_list = self.driver.find_element(By.XPATH, "//*[@id='shopify-section-1550570295841']/div/div[2]/ul")
        banner = banner_list.find_elements(By.TAG_NAME, "picture")
        self.assertEqual(4, len(banner))

    def test_element_by_xpath(self):
        self.driver.find_element(By.XPATH, "//*[@id='shopify-section-header']/div/header/div/div[2]/div/div/form/button")

    def test_shopping_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "a.site-header__icon.site-header__cart svg.icon.icon-cart")
    
    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main(verbosity=2, testRunner = HTMLTestRunner(output='reportes', report_name='search_test'))