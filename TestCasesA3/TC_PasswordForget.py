import unittest
import time
from selenium import webdriver


class ESU_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("http://dscarlson.pythonanywhere.com/login")
       elem = driver.find_element_by_xpath("html/body/div/div/div/p/a").click()
       time.sleep(5)
       elem = driver.find_element_by_id("id_email")
       elem.send_keys("danielmitchell@unomaha.edu")
       elem = driver.find_element_by_xpath("html/body/div/div/div/form/p[2]/input").click()
       assert "Forgot Password"

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
