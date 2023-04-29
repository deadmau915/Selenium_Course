import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.ui import Select

class Dropdown_And_Lists(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://madison-island.com/")

    def test_select_womens_items(self):
        self.driver.find_element(By.XPATH, "(//a[@href='/collections/women'])[3]").click()
        exp_options = ['All products', 'Dresses & Skirts', 'New arrivals', 'Pants & Denim', 'Tops & Blouses', 'Women']
        act_options = []
        
        select_kindOf_product = Select(self.driver.find_element(By.ID, 'FilterTags'))
        self.assertEqual(6, len(select_kindOf_product.options))

        for option in select_kindOf_product.options:
            act_options.append(option.text)
        
        self.assertListEqual(exp_options, act_options)

        self.assertEqual('All products', select_kindOf_product.first_selected_option.text)

        select_kindOf_product.select_by_visible_text('New arrivals')

        self.assertTrue('new-arrivals' in self.driver.current_url)

        select_kindOf_product = Select(self.driver.find_element(By.ID, 'FilterTags'))
        select_kindOf_product.select_by_index(0)
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='DropdownAndList'))