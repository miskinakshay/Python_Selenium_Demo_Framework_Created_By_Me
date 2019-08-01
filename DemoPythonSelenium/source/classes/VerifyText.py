import unittest
import HtmlTestRunner
from source.classes.SelectBrowser import selectbrowser
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException



class verifytext:

    @classmethod
    def test_VerifyTextByXpath(self,XpathValue,PageText):
        s1=selectbrowser.driver.find_element_by_xpath(XpathValue)     #get Text
        s2=s1.text

        if(s2==PageText):
            print("Match")
        else:
            print("Heading Text Not Matching",NoSuchElementException)

    @classmethod
    def test_VerifyTextByID(self,IDValue,PageText):
        s1 = selectbrowser.driver.find_element_by_id(IDValue)  # get Text
        s2 = s1.text

        if (s2 == PageText):
            print("Match")
        else:
            print("Heading Text Not Matching", NoSuchElementException)

    @classmethod
    def test_VerifyTextByClassName(self,ClassValue,PageText):
        s1 = selectbrowser.driver.find_element_by_class_name(ClassValue)  # get Text
        s2 = s1.text

        if (s2 == PageText):
            print("Match")
        else:
            print("Heading Text Not Matching", NoSuchElementException)




