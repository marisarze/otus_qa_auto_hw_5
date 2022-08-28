import pytest
from conftest import driver, url
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from exception_wrappers import wait, wait_title


def test_main(driver, url):
    driver.get(url=url)
    driver.save_screenshot("test.png")
    assert driver.title == "Your Store"
    wait
