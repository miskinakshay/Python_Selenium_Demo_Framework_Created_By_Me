from selenium import webdriver
from source.classes.General_Function import general_function
import unittest
import HtmlTestRunner
import time
from source.classes.SelectBrowser import selectbrowser
from source.classes.OpenBrowser import openbrowser
from source.pages.pageOpenBrowser import pageopenbrowser
from source.classes.VerifyText import verifytext
from source.classes.CloseBrowser import closebrowser
from source.classes.General_Function import general_function
from source.classes.WriteDataOnExcel import writeDataOnExcel

#if __name__ == '__main__':
#    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Administrator/PycharmProjects/DemoPythonSelenium/Report'))
#selectbrowser.test_selectFireFoxBrowser()     #.......problem occure.....
    #selectbrowser.test_selectIEBrowser()
    #openbrowser.test_openurl(pageopenbrowser.RegistrationURl)



    #general_function.test_TextBoxByName("firstName",'amit')
    #general_function.test_ButtonClickByName('register')

    #general_function.test_DropDownByText_UsingXpath("//select[@name='country']","BOSNIA AND HERZEGOVINA ")

    #general_function.test_DropDownByText("country","BOSNIA AND HERZEGOVINA ")

    #general_function.test_ButtonClickByXpath("//input[@name='register']")

    #general_function.test_ClickOnLink("SIGN-OFF")

class abc():
    selectbrowser.test_selectChromeBrowser()
    openbrowser.test_openurl(pageopenbrowser.test)
    verifytext.test_VerifyTextByClassName("banner__headline", "5 Common SEO Mistakes with Web Page Titles")
    #writeDataOnExcel.test_WriteDataOnExcel()
    general_function.test_DropDownByText_UsingXpath("//select[@id='blog-cat-dropdown']","SOCIAL MEDIA")

    verifytext.test_VerifyTextByXpath("//h1[contains(text(),'5 Types of Social Media and Examples of Each')]","5 Types of Social Media and Examples of Each")
    general_function.test_TextBoxByName("_Email","xyz@gmail.com")
    general_function.test_ButtonClickByXpath("//button[@class='btn yellow']")
    closebrowser.test_CloseBrowser()











