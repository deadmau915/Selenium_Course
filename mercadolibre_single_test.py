import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pyunitreport import HTMLTestRunner

class MercadoLibreTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://mercadolibre.com/")

    def test_mercadolibre(self):
        driver = self.driver
        country = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "CO")))
        country.click()

        search_bar = driver.find_element(By.ID, "cb1-edit")
        search_bar.send_keys("Playstation 4")
        search_bar.submit()
    
    def tearDown(self):
        self.driver.close()
    
if __name__=="__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="mercadolibre_singletest"))