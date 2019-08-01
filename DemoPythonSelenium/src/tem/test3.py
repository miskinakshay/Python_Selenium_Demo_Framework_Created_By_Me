

#from selenium import webdriver

import unittest
import HtmlTestRunner

class test33(unittest.TestCase):
    a=0
    def test_A(name):
        print("hello A",a)

    def test_B(age):
        print("python B",age)

    def test_C():
            print("hello C")

    def test_D():
            print("python D")
"""
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Administrator/PycharmProjects/DemoPythonSelenium/Report'))

"""