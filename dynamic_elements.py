import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner

class DynamicElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Disappearing Elements').click()

    def test_name_elements(self):
        driver = self.driver

        options = []
        menu = 5
        tries = 1

        while len(options) < 5:
            options.clear()

            for i in range(menu):
                try:
                    option_name = driver.find_element(By.XPATH, f'(//li)[{i + 1}]')
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f'option number {i+1} is NOT FOUND')
                    tries += 1
                    driver.refresh()
            
        print(f'Finish in {tries} tries')
    
    def tearDown(self):
        self.driver.close()
    
if __name__=='__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='DynamicElementstest'))