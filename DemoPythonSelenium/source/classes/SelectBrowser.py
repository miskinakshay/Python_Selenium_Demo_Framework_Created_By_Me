
import unittest
import HtmlTestRunner
from selenium import webdriver
from source.pages.pageSelectBrowser import pageselectbrowser



class selectbrowser:

    @classmethod
    def test_selectChromeBrowser(cls):
        cls.driver = webdriver.Chrome(executable_path=pageselectbrowser.Chromepath)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def test_selectFireFoxBrowser(cls):
        cls.driver = webdriver.Firefox(executable_path=pageselectbrowser.FireFoxpath)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    @classmethod
    def test_selectIEBrowser(cls):
        cls.driver = webdriver.Ie(executable_path=pageselectbrowser.IEpath)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()



"""
    it will be run only once before every test method.
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path='C:/Users/Administrator/Desktop/Katalon_Studio_Windows_64-6.1.5 (1)/Katalon_Studio_Windows_64-6.1.5/configuration/resources/drivers/chromedriver_win32/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
   """

