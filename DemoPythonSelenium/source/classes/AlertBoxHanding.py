
import unittest
import HtmlTestRunner
from selenium import webdriver
from source.classes.SelectBrowser import selectbrowser

class alertbochanding(unittest.TestCase):

    @classmethod
    def test_AlertBoxHandle(self):
        obj = selectbrowser.driver.switch_to.alert
        obj.accept()
