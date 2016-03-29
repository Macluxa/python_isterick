#-*- coding: utf -*-

from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group
from application import Application


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_new_group(unittest.TestCase):

    def setUp(self):
        self.app = Application()

    def test_test_new_group(self):
        self.app.login('admin', 'secret')
        self.app.create_group(Group(name='test test', header='test test', footer='test test'))

    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()