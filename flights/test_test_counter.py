from unittest import TestCase
from selenium import webdriver

driver = webdriver.Chrome()

class Test(TestCase):
    def test_counter(self):
        driver.get("http://127.0.0.1:8000/flights/counter")
        increase = driver.find_element_by_id("increase")
        increase.click()
        self.assertEqual(driver.find_element_by_id("result").text,"1")

