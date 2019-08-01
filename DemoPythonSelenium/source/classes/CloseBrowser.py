

import unittest
import HtmlTestRunner
from selenium import webdriver
from source.classes.SelectBrowser import selectbrowser
import time

from selenium.webdriver.support.ui import Select

class closebrowser:
    @classmethod
    def test_CloseBrowser(self):
        time.sleep(2)
        selectbrowser.driver.quit()

