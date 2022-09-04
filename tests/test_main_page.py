import pytest
import time
from conftest import driver, url
from selenium.webdriver.common.by import By
from exception_wrappers import *
from selenium.webdriver.common.action_chains import ActionChains


def test_home_button(driver, url):
    driver.get(url=url)
    home_button = driver.find_element(by=By.CSS_SELECTOR, value='#logo > a')
    assert home_button.get_attribute('href') == 'http://192.168.0.102:8081/index.php?route=common/home'


def test_navbar_elements(driver, url):
    driver.get(url=url)
    navbar = driver.find_element(by=By.CSS_SELECTOR, value=".collapse.navbar-collapse>.nav.navbar-nav")
    navbar_elems = navbar.find_elements(by=By.CSS_SELECTOR, value=".nav.navbar-nav > li")
    assert len(navbar_elems)==8
    
    desktops_ref = navbar_elems[0].find_element(by=By.TAG_NAME, value="a")
    href_result = desktops_ref.get_attribute("href")
    href_expectation = url+"/desktops"
    assert href_result == href_expectation
    assert desktops_ref.text == "Desktops"    
    
    mp3players_ref = navbar_elems[-1].find_element(by=By.TAG_NAME, value="a")
    href_result = mp3players_ref.get_attribute("href")
    href_expectation = url+"/mp3-players"
    assert href_result == href_expectation
    assert mp3players_ref.text == "MP3 Players"
    
    navbar_elems[4].click()
    left_column_software_ref = wait((By.XPATH, '//*[@id="column-left"]/div[1]/a[5]'), driver)
    assert left_column_software_ref.text.startswith('Software')
    assert left_column_software_ref.get_attribute('href').startswith(url+'/software')
    assert 'active' in left_column_software_ref.get_attribute('class')
    driver.back()
    wait((By.CSS_SELECTOR, "#slideshow0 > div"), driver)
    
    navbar_elems[5].click()
    left_column_phones_pdas_ref = wait((By.XPATH, '//*[@id="column-left"]/div[1]/a[6]'), driver)
    assert left_column_phones_pdas_ref.text.startswith('Phones & PDAs')
    assert left_column_phones_pdas_ref.get_attribute('href').startswith(url+'/smartphone')
    assert 'active' in left_column_phones_pdas_ref.get_attribute('class')
    driver.back()
    wait((By.CSS_SELECTOR, "#slideshow0 > div"), driver)


def test_featured_elements(driver, url):
    driver.get(url=url)
    featured_elems = driver.find_elements(by=By.CSS_SELECTOR, value='#content > div.row > div.product-layout')
    assert len(featured_elems)==4
    for i, elem in enumerate(featured_elems):
        ref_image = wait((By.CSS_SELECTOR, 'div > div.image > a'), driver)
        ActionChains(driver).move_to_element(ref_image).click().perform()
        add_to_cart_button = wait((By.CSS_SELECTOR, '#button-cart'), driver)
        assert add_to_cart_button.text=='Add to Cart'
        driver.back()
        wait((By.CSS_SELECTOR, '#content > div.row > div.product-layout'), driver)
        wish_list_add_button = elem.find_element(by=By.CSS_SELECTOR, value='div > div.button-group > button:nth-child(2)')
        wish_list_add_button.click()
        alert = wait((By.CSS_SELECTOR, '#common-home > div.alert.alert-success.alert-dismissible'), driver)
        
        assert "You must" in alert.text
        alert_close_button = driver.find_element(by=By.CSS_SELECTOR, value='#common-home > div.alert.alert-success.alert-dismissible > button')
        alert_close_button.click()
        wait_not((By.CSS_SELECTOR, '#common-home > div.alert.alert-success.alert-dismissible > button'), driver)


def test_basket(driver, url):
    driver.get(url=url)
    basket_button = driver.find_element(by=By.CSS_SELECTOR, value='#cart > button')
    if basket_button.text=="0 item(s) - $0.00":
        basket_button.click()
        notification = wait((By.CSS_SELECTOR, '#cart > ul > li > p'), driver)
        assert notification.text == 'Your shopping cart is empty!'


# driver_folder = r"C:\Users\marisarze\Downloads\browsers"
# driver = webdriver.Chrome(executable_path=driver_folder+'/chromedriver.exe')
# url = r"http://192.168.0.102:8081"
# test_home_button(driver, url)

# driver_folder = r"C:\Users\marisarze\Downloads\browsers"
# driver = webdriver.Chrome(executable_path=driver_folder+'/chromedriver.exe')
# url = r"http://192.168.0.102:8081"
# test_navbar_elements(driver, url)

# driver_folder = r"C:\Users\marisarze\Downloads\browsers"
# driver = webdriver.Chrome(executable_path=driver_folder+'/chromedriver.exe')
# url = r"http://192.168.0.102:8081"
# test_featured_elements(driver, url)

# driver_folder = r"C:\Users\marisarze\Downloads\browsers"
# driver = webdriver.Chrome(executable_path=driver_folder+'/chromedriver.exe')
# url = r"http://192.168.0.102:8081"
# test_basket(driver, url)