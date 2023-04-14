import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from pyunitreport import HTMLTestRunner

class MercadoLibreTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://mercadolibre.com/")

    def test_mercadolibre(self):
        driver = self.driver
        country = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "CO")))
        country.click()

        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '(//button[contains(@class, "cookie-consent-banner")])[1]'))).click()
        except:
            print("You already accepted the cookies in this website")

        search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cb1-edit")))
        search_bar.send_keys("Playstation 4")
        search_bar.submit()

        filter_condition_new = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@aria-label="Nuevo"]')))
        filter_condition_new.click()

        self.assertTrue(self.is_element_present(By.TAG_NAME, '//div[@class="andes-tag__label"]'))
    
    @classmethod
    def tearDown(cls):
        cls.driver.close()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True
    
if __name__=="__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="mercadolibre_singletest"))