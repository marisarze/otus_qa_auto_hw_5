from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


def wait(selector, driver, method=EC.visibility_of_element_located, by=By.CSS_SELECTOR, timeout=5, screenshot=False):
    try:
        return WebDriverWait(driver, timeout).until(method(by, selector))
    except:
        if screenshot:
            driver.save_screenshot("{}.png".format(driver.session_id))
        raise AssertionError(f"Didn't wait: {method.__name__}")


def wait_title(title, driver, timeout=3):
    try:
        WebDriverWait(driver, timeout).until(EC.title_is(title))
    except:
        raise AssertionError(f"Expected to get the title {title} but it is {driver.title}")
