from selenium import webdriver
import unittest
import HtmlTestRunner


class googlee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path='C:/Users/Administrator/Desktop/Katalon_Studio_Windows_64-6.1.5 (1)/Katalon_Studio_Windows_64-6.1.5/configuration/resources/drivers/chromedriver_win32/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_gmail(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name('q').send_keys('gmail')
        self.driver.find_element_by_name('btnK').click()


    def test_facebook(self):
        self.driver.get("https://www.facebook.com/")
        self.driver.find_element_by_xpath("//a[contains(text(),'Create a Page')]").click()

    def test_google(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name('q').send_keys('Facebook')
        self.driver.find_element_by_name('btnK').click()

    def test_yahoo(self):
        self.driver.get("https://in.yahoo.com/?p=us")
        self.driver.find_element_by_name("p").send_keys("selenium python webdriver tpoint")
        self.driver.find_element_by_xpath("//button[@id='uh-search-button']").click()



# main funtion is to be difine in test2.py file
#if __name__ == '__main__':
#    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Administrator/PycharmProjects/DemoPythonSelenium/src/Result'))

