import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner

class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Typos').click()

    def test_find_typos(self):
        driver = self.driver
        paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')
        text_to_check = paragraph_to_check.text
        self.assertTrue(isinstance(text_to_check, str))

        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while not found:
            if text_to_check == correct_text:
                found = True
            else:
                tries += 1
                driver.refresh()
                text_to_check = self.driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)').text
        
        print(f'It took {tries} tries to find the typo')
    
    def tearDown(self):
        self.driver.close()
    
if __name__=='__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='test_typos'))