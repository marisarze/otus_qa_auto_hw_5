import pytest
from conftest import driver, url
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from exception_wrappers import *

def test_register_button(driver, url):
    driver.get(url=url)
    dropdown_register_login = driver.find_element(by=By.CSS_SELECTOR, value='#top-links > ul > li.dropdown')
    dropdown_register_login.click()
    register_ref = driver.find_element(by=By.CSS_SELECTOR, value='#top-links > ul > li.dropdown.open > ul > li:nth-child(1)')
    register_ref.click()
    page_h1_name = wait((By.CSS_SELECTOR, '#content > h1'), driver)
    assert page_h1_name.text == 'Register Account'


def test_registration(driver, url):
    driver.get(url=url+'/index.php?route=account/register')

    first_name_label = driver.find_element(by=By.CSS_SELECTOR, value='#account > div:nth-child(3) > label')
    assert first_name_label.text == 'First Name'
    first_name_input = driver.find_element(by=By.CSS_SELECTOR, value='#input-firstname')
    first_name_input.send_keys("Donald")

    last_name_label = driver.find_element(by=By.CSS_SELECTOR, value='#account > div:nth-child(4) > label')
    assert last_name_label.text == 'Last Name'
    last_name_input = driver.find_element(by=By.CSS_SELECTOR, value='#input-lastname')
    last_name_input.send_keys("Duck")

    email_label = driver.find_element(by=By.CSS_SELECTOR, value='#account > div:nth-child(5) > label')
    assert email_label.text == 'E-Mail'
    email_input = driver.find_element(by=By.CSS_SELECTOR, value='#input-email')
    email_input.send_keys("richbird@mail.com")

    phone_label = driver.find_element(by=By.CSS_SELECTOR, value='#account > div:nth-child(6) > label')
    assert phone_label.text == 'Telephone'
    phone_input = driver.find_element(by=By.CSS_SELECTOR, value='#input-telephone')
    phone_input.send_keys("12345678901")

    password_label = driver.find_element(by=By.CSS_SELECTOR, value='#content > form > fieldset:nth-child(2) > div:nth-child(2) > label')
    assert password_label.text == 'Password'
    password_input = driver.find_element(by=By.CSS_SELECTOR, value='#input-password')
    password_input.send_keys("quackquack")

    password_confirm_label = driver.find_element(by=By.CSS_SELECTOR, value='#content > form > fieldset:nth-child(2) > div:nth-child(3) > label')
    assert password_confirm_label.text == 'Password Confirm'
    password_confirm_input = driver.find_element(by=By.CSS_SELECTOR, value='#input-confirm')
    password_confirm_input.send_keys("quackquack")

    privacy_policy_check = driver.find_element(by=By.CSS_SELECTOR, value='#content > form > div > div > input[type=checkbox]:nth-child(2)')
    privacy_policy_check.click()

    continue_button = driver.find_element(by=By.CSS_SELECTOR, value='#content > form > div > div > input.btn.btn-primary')
    continue_button.click()

    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '//*[@id="content"]/h1[contains(text(), "Your Account Has Been Created!")]')))
    except TimeoutException:
        warning = wait((By.CSS_SELECTOR, '#account-register > div.alert.alert-danger.alert-dismissible'), driver)
        assert warning.text == 'Warning: E-Mail Address is already registered!'

