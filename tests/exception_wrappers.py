from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

def wait(locator, driver, *args, method=EC.visibility_of_element_located, timeout=5, screenshot=True):
    try:
        return WebDriverWait(driver, timeout).until(method(locator, *args))
    except TimeoutException:
        if screenshot:
            driver.save_screenshot("{}.png".format(driver.session_id+str(time.time)))
        raise AssertionError(f"Didn't wait: {method.__name__}")


def wait_not(locator, driver, *args, method=EC.visibility_of_element_located, timeout=5, screenshot=True):
    try:
        return WebDriverWait(driver, timeout).until_not(method(locator, *args))
    except TimeoutException:
        if screenshot:
            driver.save_screenshot("{}.png".format(driver.session_id+str(time.time)))
        raise AssertionError(f"Didn't wait: {method.__name__}")


def wait_title(title, driver, timeout=3):
    try:
        WebDriverWait(driver, timeout).until(EC.title_is(title))
    except TimeoutException:
        raise AssertionError(f"Expected to get the title {title} but it is {driver.title}")
