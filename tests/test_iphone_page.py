from logging import addLevelName
import pytest
from conftest import driver, url
from selenium.webdriver.common.by import By
from exception_wrappers import *


def test_product_name(driver, url):
    driver.get(url=url)
    iphone_ref = driver.find_element(by=By.CSS_SELECTOR, value='#content > div.row > div:nth-child(2) > div > div.image > a')
    iphone_ref.click()

    product_name = wait((By.CSS_SELECTOR, '#content > div:nth-child(1) > div.col-sm-4 > h1'), driver)
    assert product_name.text == "iPhone"


def test_add_to_cart(driver, url):
    driver.get(url=url+'/iphone')

    add_to_cart_button = driver.find_element(by=By.CSS_SELECTOR, value='#button-cart')
    add_to_cart_button.click()
    success_alert = wait((By.CSS_SELECTOR, '#product-product > div.alert.alert-success.alert-dismissible'), driver)
    assert "You have added" in success_alert.text


def test_wish_list(driver, url):
    driver.get(url=url+"/iphone")

    wishlist_button = driver.find_element(by=By.CSS_SELECTOR, value='#content > div:nth-child(1) > div.col-sm-4 > div.btn-group > button:nth-child(1)')
    wishlist_button.click()
    wait((By.XPATH, '//div[contains(text(), " You must ")]'), driver)


def test_related_products(driver, url):
    driver.get(url=url+'/iphone')

    related_object_header = driver.find_element(by=By.CSS_SELECTOR, value='#content > h3')
    assert related_object_header.text == 'Related Products'

    related_object_image_ref = driver.find_element(by=By.CSS_SELECTOR, value='#content > div:nth-child(3) > div > div > div.image > a')
    assert related_object_image_ref.get_attribute('href').startswith(url)

    product_image = driver.find_element(by=By.CSS_SELECTOR, value='#content > div:nth-child(1) > div.col-sm-8 > ul.thumbnails > li:nth-child(1) > a')
    assert product_image.get_attribute('href').endswith('.jpg')
