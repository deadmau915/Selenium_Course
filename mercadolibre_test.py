import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
from mercadolibre_page import MercadoLibrePage

class MercadoLibreTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_mercadolibre_flowpage(self):
        mcl = MercadoLibrePage(self.driver)
        mcl.open()
        mcl.select_country('colombia')
        mcl.accept_cookies()
        mcl.search_product('playstation 4')
        mcl.set_filter('bogotá d.c.')
        mcl.set_filter('nuevo')
        mcl.sort_by('mayor precio')
        mcl.get_first_5_items()
        self.driver.find_element().get_property()
    
    @classmethod
    def tearDown(cls):
        cls.driver.close()
    
if __name__=="__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="mercadolibre_test"))