
import unittest
import HtmlTestRunner
from selenium import webdriver
from source.classes.SelectBrowser import selectbrowser

from selenium.webdriver.support.ui import Select

class general_function:

    @classmethod
    def test_TextBoxByName(self,AttributeValue,UserInput):
        selectbrowser.driver.find_element_by_name(AttributeValue).send_keys(UserInput)

    @classmethod
    def test_textBoxByID(self,AttributeValue,UserInput):
        selectbrowser.driver.find_element_by_id(AttributeValue).send_keys(UserInput)

    @classmethod
    def test_textBoxByXpath(self,XpathValue,UserInput):
        selectbrowser.driver.find_element_by_xpath(XpathValue).send_keys(UserInput)


    @classmethod
    def test_ButtonClickByName(self,AttributeValue):
        selectbrowser.driver.find_element_by_name(AttributeValue).click()

    @classmethod
    def test_ButtonClickByID(self, AttributeValue):
        selectbrowser.driver.find_element_by_id(AttributeValue).click()

    @classmethod
    def test_ButtonClickByXpath(self,XpathValue):
        selectbrowser.driver.find_element_by_xpath(XpathValue).click()

    @classmethod
    def test_DropDwonByID(self, AttributeValue, IndexNumber):
        s1 = Select(selectbrowser.driver.find_element_by_name(AttributeValue))
        s1.select_by_index(IndexNumber)

    @classmethod
    def test_DropDwonByID(self, AttributeValue, IndexNumber):
        s1 = Select(selectbrowser.driver.find_element_by_name(AttributeValue))
        s1.select_by_index(IndexNumber)

    @classmethod
    def test_DropDownByValue(self, AttributeValue, ValueName):
        s1 = Select(selectbrowser.driver.find_element_by_name(AttributeValue))
        s1.select_by_value(ValueName)

    @classmethod
    def test_DropDownByText(self, AttributeValue, OptionName):
        s1 = Select(selectbrowser.driver.find_element_by_name(AttributeValue))
        s1.select_by_visible_text(OptionName)

    @classmethod
    def test_DropDwonByID_UsingXpth(self, AttributeValue, IndexNumber):
        s1 = Select(selectbrowser.driver.find_element_by_xpath(AttributeValue))
        s1.select_by_index(IndexNumber)

    @classmethod
    def test_DropDownByValue_UsingXpth(self, AttributeValue, ValueName):
        s1 = Select(selectbrowser.driver.find_element_by_xpath(AttributeValue))
        s1.select_by_value(ValueName)

    @classmethod
    def test_DropDownByText_UsingXpath(self, AttributeValue, OptionName):
        s1 = Select(selectbrowser.driver.find_element_by_xpath(AttributeValue))
        s1.select_by_visible_text(OptionName)

    @classmethod
    def test_ClickOnLink(self,LinkText):
        selectbrowser.driver.find_element_by_link_text(LinkText).click()

        #link=driver.find_element_by_xpath(.//*[@id="content"]/div[3]/div/div/div[2]/h4)
        #link.click()

    @classmethod
    def test_ClickOnRedioButton(self,XpathValue):
        selectbrowser.driver.find_element_by_xpath(XpathValue).click()

    @classmethod
    def test_SelectCheckBox(Self,XpathValue):
        selectbrowser.driver.find_element_by_xpath(XpathValue).click()
























