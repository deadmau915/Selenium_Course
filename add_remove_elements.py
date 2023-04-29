import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner

class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        
    def test_add_remove(self):
        driver = self.driver
        
        elements_added = int(input('how many elements will you add?: '))
        elements_removed = int(input('How many elements will you remove?: '))
        total_elements = elements_added - elements_removed
        add_button = driver.find_element(By.XPATH, '//button[@onclick="addElement()"]')

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element(By.XPATH, '(//button[@class="added-manually"])[1]')
                delete_button.click()
            except:
                print("you triying to delete more elements than the existent")
                break

        if total_elements > 0:
            print(f"there are {total_elements} elements on scree")
        else:
            print('There are 0 elements on screen')
    
    def tearDown(self):
        self.driver.close()
    
if __name__=='__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='AddRemoveElements'))