from logging import addLevelName
import pytest
import time
from conftest import driver, url
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from exception_wrappers import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select



def test_login_button(driver, url):
    driver.get(url=url)
    dropdown_register_login = driver.find_element(by=By.CSS_SELECTOR, value='#top-links > ul > li.dropdown')
    dropdown_register_login.click()
    login_ref = driver.find_element(by=By.CSS_SELECTOR, value='#top-links > ul > li.dropdown.open > ul > li:nth-child(2)')
    login_ref.click()

    left_part_head = wait((By.CSS_SELECTOR, '#content > div > div:nth-child(1) > div > h2'), driver)
    assert left_part_head.text == 'New Customer'


def test_login_fields(driver, url):
    driver.get(url=url+'/index.php?route=account/login')

    right_part_head = wait((By.CSS_SELECTOR, '#content > div > div:nth-child(2) > div > h2'), driver)
    assert right_part_head.text == 'Returning Customer'

    email_input = driver.find_element(by=By.CSS_SELECTOR, value='#input-email')
    email_input.send_keys("richbird@mail.com")

    password_input = driver.find_element(by=By.CSS_SELECTOR, value='#input-password')
    password_input.send_keys("quackquack")

    login_confirm_button = driver.find_element(by=By.CSS_SELECTOR, value='#content > div > div:nth-child(2) > div > form > input')
    login_confirm_button.click()

    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/h2[contains(text(), "My Affiliate Account")]')))
    except TimeoutException:
        warning = wait((By.CSS_SELECTOR, '#account-login > div.alert.alert-danger.alert-dismissible'), driver)
        assert warning.text == 'Warning: No match for E-Mail Address and/or Password.'

from selenium import webdriver
# driver_folder = r"C:\Users\marisarze\Downloads\browsers"
# driver = webdriver.Chrome(executable_path=driver_folder+'/chromedriver.exe')
# url = r"http://192.168.0.102:8081"
# test_login_button(driver, url)

# driver_folder = r"C:\Users\marisarze\Downloads\browsers"
# driver = webdriver.Chrome(executable_path=driver_folder+'/chromedriver.exe')
# url = r"http://192.168.0.102:8081"
# test_login_fields(driver, url)