#-*_ coding: utf -*-

from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_new_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_test_new_group(self):
        success = True
        wd = self.wd
        wd.get('http://localhost/addressbook/')
        wd.find_element_by_name("user").click()





    def tearDown(self):
        self.wd.qiut()

if __name__ == '__main__':
    unittest.main()