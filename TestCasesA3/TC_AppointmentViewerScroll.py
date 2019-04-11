import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ESU_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "instructor"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://dscarlson.pythonanywhere.com/login")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       time.sleep(5)
       elem = driver.find_element_by_xpath("html/body/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a").click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("html/body/div/div/div/div/a[2]").click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("html/body/div/div/div/div/a[2]").click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("html/body/div/div/div/div/a[3]").click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("html/body/div/div/div/div/a").click()

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
