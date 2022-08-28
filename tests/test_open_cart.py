import pytest
from conftest import driver, url
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from exception_wrappers import wait, wait_title

from selenium import webdriver
driver_folder = r"C:\Users\marisarze\Downloads\browsers"
driver = webdriver.Chrome(executable_path=driver_folder+'/chromedriver.exe')
url = "http:\/\/192.168.0.102:8081\/"

def test_main(driver, url):
    driver.get(url=url)
    driver.save_screenshot("test.png")
    assert driver.title == "Your Store"
    navbar = driver.find_element(by=By.CSS_SELECTOR, value=".collapse.navbar-collapse>.nav.navbar-nav")
    li_nav_elements = navbar.find_elements(by=By.CSS_SELECTOR, value=".nav.navbar-nav > li")
    for i, elem in enumerate(li_nav_elements):
        print(i, elem.__dict__)

test_main(driver, url)