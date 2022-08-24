import pytest
from conftest import driver, url
from selenium.webdriver.common.by import By



def test_main(driver, url):
    driver.get(url=url)
    driver.save_screenshot("test.png")
    assert driver.title == "Your Store"
