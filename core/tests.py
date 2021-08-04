from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.

class SeleniumTest(TestCase):
    def test_one(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_link_text("Create").click()
        name = driver.find_element_by_name('name')
        name.send_keys('Test note')

        location = driver.find_element_by_name('location')
        location.send_keys('Test note')

        description = driver.find_element_by_name('descriprion')
        description.send_keys('Test place description')

        button = driver.find_element_by_tag_name('button')
        button.click()
        
        sleep(5)

        driver.close()


class ProfileTestCase(TestCase):
    def test_open_profile_edit(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/profile/")

        element = driver.find_element_by_xpath("//*[contains(text(), 'Edit')]")
        element.click()

        