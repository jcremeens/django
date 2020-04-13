import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[1]/a/span").click()
        time.sleep(5)
        elem = driver.find_element_by_id("id_title")
        elem.send_keys("This is a test post with selenium")
        elem = driver.find_element_by_id("id_text")
        elem.send_keys("This is a test post of text with selenium")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
        time.sleep(5)
        assert "Posted Blog Entry"
        driver.get("http://127.0.0.1:8000")
        time.sleep(1)
        driver.get("http://127.0.0.1:8000")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[4]/h2/a").click()
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/a/span").click()
        time.sleep(5)
        elem = driver.find_element_by_id("id_title")
        elem.send_keys(". This is a test *read* and *update* of a post with selenium")
        elem = driver.find_element_by_id("id_text")
        elem.send_keys(". This is a test *read* and *update* of a post of text with selenium")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
        time.sleep(5)
        driver.get("http://127.0.0.1:8000")
        time.sleep(5)
        driver.get("http://127.0.0.1:8000/admin/blog/post/")
        time.sleep(5)
        elem = driver.find_element_by_link_text("This is a test post with selenium. This is a test *read* and *update* of a post with selenium").click()
        time.sleep(5)
        elem = driver.find_element_by_link_text("Delete").click()
        time.sleep(5)
        elem = driver.find_element_by_xpath("//*[@id='content']/form/div/input[2]").click()
        time.sleep(5)
        driver.get("http://127.0.0.1:8000")
        time.sleep(5)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
