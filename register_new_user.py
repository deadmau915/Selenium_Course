import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pyunitreport import HTMLTestRunner

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://madison-island.com/')

    def test_new_user(self):
        driver = self.driver
        driver.find_element(By.XPATH, '//a[@href="/account/login"]').click()
        create_account_button = driver.find_element(By.ID, 'customer_register_link')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Create Account – madison-island', driver.title)

        first_name = driver.find_element(By.ID, 'FirstName')
        last_name = driver.find_element(By.ID, 'LastName')
        email = driver.find_element(By.ID, 'Email')
        password = driver.find_element(By.ID, 'CreatePassword')
        submit_button = driver.find_element(By.XPATH, '//input[@value="Create"]')

        self.assertTrue(first_name.is_enabled() and last_name.is_enabled()
                        and email.is_enabled() and password.is_enabled() and submit_button.is_enabled())
        
        first_name.send_keys('joe')
        last_name.send_keys('doe')
        email.send_keys('joedoe@email.com')
        password.send_keys('joedoepass@123')
        submit_button.click()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner = HTMLTestRunner(output='reportes', report_name='register_new_user_test'))
