

import unittest
from selenium import webdriver
import HtmlTestRunner
from source.classes.SelectBrowser import selectbrowser

class openbrowser(unittest.TestCase):

    @classmethod
    def test_openurl(self,url):
        selectbrowser.driver.get(url)

