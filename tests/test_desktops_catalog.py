import pytest
import time
from conftest import driver, url
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from exception_wrappers import *
from selenium.webdriver.support.ui import Select
from selenium import webdriver


def test_desktop_button(driver, url):
    driver.get(url=url)
    desktops_button = driver.find_element(by=By.CSS_SELECTOR, value='#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(1) > a')
    desktops_button.click()
    show_all_desktops_button = driver.find_element(by=By.CSS_SELECTOR, value='#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li.dropdown.open > div > a')
    show_all_desktops_button.click()
    refine_search = wait((By.CSS_SELECTOR, '#content > h3'), driver)
    assert refine_search.text == 'Refine Search'


def test_sorting_and_total(driver, url):
    driver.get(url=url+'/desktops')
    sorting_select = Select(driver.find_element(by=By.CSS_SELECTOR, value='#input-sort'))
    sorting_select.select_by_visible_text('Price (High > Low)')

    products = wait((By.CSS_SELECTOR, '#content > div:nth-child(7) > div'), driver, method=EC.visibility_of_all_elements_located)
    assert len(products)>0
    price_sum = 0
    for i in range(min(4, len(products))):
        
        price_p = wait((By.CSS_SELECTOR, f'#content > div:nth-child(7) > div:nth-child({i+1}) > div > div:nth-child(2) > div.caption > p.price'), driver)
        raw_text = price_p.text.replace(',', '').replace('.', '').replace(' ', '')
        price = int(raw_text.split('\n')[0][1:].split('$')[0])
        price_sum += price
        wait((By.CSS_SELECTOR, '#cart-total'), driver)
        add_to_cart_button = wait((By.CSS_SELECTOR, f'#content > div:nth-child(7) > div:nth-child({i+1}) > div > div:nth-child(2) > div.button-group > button:nth-child(1)'), driver, method=EC.element_to_be_clickable)
        add_to_cart_button.click()
        wait((By.CSS_SELECTOR, '#product-category > div.alert.alert-success.alert-dismissible'), driver)
        time.sleep(1)
        if i==0:
            max_price = price
        else:
            assert price<=max_price
        

    total_raw = wait((By.CSS_SELECTOR, '#cart-total'), driver).text.split('$')
    total_raw = total_raw[1]
    total = int(total_raw.replace(',', '').replace('.', ''))
    assert price_sum == total


# driver_folder = r"C:\Users\marisarze\Downloads\browsers"
# driver = webdriver.Chrome(executable_path=driver_folder+'/chromedriver.exe')
# url = r"http://192.168.0.102:8081"
# test_desktop_button(driver, url)

# driver_folder = r"C:\Users\marisarze\Downloads\browsers"
# driver = webdriver.Chrome(executable_path=driver_folder+'/chromedriver.exe')
# url = r"http://192.168.0.102:8081"
# test_sorting_and_total(driver, url)