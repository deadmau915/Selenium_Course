import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pyunitreport import HTMLTestRunner

class CompareProducts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys('tee')
        search_field.submit()
        
        driver.find_element(By.XPATH, '(//a[@class="link-compare"])[1]').click()
        driver.find_element(By.XPATH, '(//a[contains(@onclick, "return confirm")])[2]').click()

        alert = driver.switch_to.alert
        alert_text = alert.text

        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)

        alert.accept()

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="alerts_report"))