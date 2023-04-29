import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner

class Tables(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Sortable Data Tables').click()
    
    def test_sort_tables(self):
        driver = self.driver

        table_data = [[] for i in range(5)]

        print(table_data)

        for i in range(5):
            header = driver.find_element(By.XPATH, f'(//th[@class="header"])[{i+1}]/span')
            table_data[i].append(header.text)
            for j in range(4):
                row_data = driver.find_element(By.XPATH, f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{i+1}]')
                table_data[i].append(row_data.text)

        print(table_data)
    
    def tearDown(self):
        self.driver.close()
    
if __name__=='__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='table_test'))