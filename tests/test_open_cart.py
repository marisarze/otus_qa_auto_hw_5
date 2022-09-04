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
from selenium import webdriver


def test_main(driver, url):
    driver.get(url=url)
    driver.save_screenshot("test.png")
    assert driver.title == "Your Store"
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

    featured_elems = driver.find_elements(by=By.CSS_SELECTOR, value='#content > div.row > div.product-layout')
    assert len(featured_elems)==4
    for i, elem in enumerate(featured_elems):
        ref_image = wait((By.CSS_SELECTOR, 'div > div.image > a'), driver)
        #time.sleep(1)
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
        
        

    # carousel_items = driver.find_elements(by=By.CSS_SELECTOR, value='#carousel0 > div > div')

    # def carousel_rounded(locator, old_items):

    #     def utility_function(driver):
    #         new_items = driver.find_elements(*locator)
    #         assert len(new_items)==len(old_items)
    #         for i, old_item in enumerate(old_items):
    #             if 'swiper-slide-active' in old_item.get_attribute('class'):
    #                 old_index = int(old_item.get_attribute('data-swiper-slide-index'))
    #         for i, new_item in enumerate(new_items):
    #             if 'swiper-slide-active' in new_item.get_attribute('class'):
    #                 new_index = int(new_item.get_attribute('data-swiper-slide-index'))
    #         print(old_index, new_index)
    #         if new_index == (old_index+1) % 10:
    #             return True
    #         return False
        
    #     return utility_function


    #carousel_right_button = driver.find_element(by=By.CSS_SELECTOR, value='#content > div.carousel.swiper-viewport > div.swiper-pager > div.swiper-button-next')
    #carousel_element_buttons = driver.find_elements(by=By.CSS_SELECTOR, value='#content > div.carousel.swiper-viewport > div.swiper-pagination.carousel0.swiper-pagination-clickable.swiper-pagination-bullets > span')
    #carousel_right_button.click()
    # for i, button in enumerate(carousel_element_buttons):
    #     if 'swiper-pagination-bullet-active' in button.get_attribute('class'):
    #         carousel_element_buttons[(i+1)%len(carousel_element_buttons)].click()
    #         break
    # wait((By.CSS_SELECTOR, '#carousel0 > div > div'), driver, carousel_items, method=carousel_rounded)

    basket_button = driver.find_element(by=By.CSS_SELECTOR, value='#cart > button')
    if basket_button.text=="0 item(s) - $0.00":
        basket_button.click()
        notification = wait((By.CSS_SELECTOR, '#cart > ul > li > p'), driver)
        assert notification.text == 'Your shopping cart is empty!'
    driver.close()



def test_iphone_page(driver, url):
    driver.get(url=url)
    iphone_ref = driver.find_element(by=By.CSS_SELECTOR, value='#content > div.row > div:nth-child(2) > div > div.image > a')
    iphone_ref.click()

    product_name = wait((By.CSS_SELECTOR, '#content > div:nth-child(1) > div.col-sm-4 > h1'), driver)
    assert product_name.text == "iPhone"

    add_to_cart_button = driver.find_element(by=By.CSS_SELECTOR, value='#button-cart')
    add_to_cart_button.click()
    success_alert = wait((By.CSS_SELECTOR, '#product-product > div.alert.alert-success.alert-dismissible'), driver)
    assert "You have added" in success_alert.text

    wishlist_button = driver.find_element(by=By.CSS_SELECTOR, value='#content > div:nth-child(1) > div.col-sm-4 > div.btn-group > button:nth-child(1)')
    wishlist_button.click()
    wait((By.XPATH, '//div[contains(text(), " You must ")]'), driver)

    related_object_header = driver.find_element(by=By.CSS_SELECTOR, value='#content > h3')
    assert related_object_header.text == 'Related Products'

    related_object_image_ref = driver.find_element(by=By.CSS_SELECTOR, value='#content > div:nth-child(3) > div > div > div.image > a')
    assert related_object_image_ref.get_attribute('href').startswith(url)

    product_image = driver.find_element(by=By.CSS_SELECTOR, value='#content > div:nth-child(1) > div.col-sm-8 > ul.thumbnails > li:nth-child(1) > a')
    assert product_image.get_attribute('href').endswith('.jpg')


def test_register_page(driver, url):
    driver.get(url=url)
    dropdown_register_login = driver.find_element(by=By.CSS_SELECTOR, value='#top-links > ul > li.dropdown')
    dropdown_register_login.click()
    register_ref = driver.find_element(by=By.CSS_SELECTOR, value='#top-links > ul > li.dropdown.open > ul > li:nth-child(1)')
    register_ref.click()
    page_h1_name = wait((By.CSS_SELECTOR, '#content > h1'), driver)
    assert page_h1_name.text == 'Register Account'

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
    time.sleep(1)

    continue_button = driver.find_element(by=By.CSS_SELECTOR, value='#content > form > div > div > input.btn.btn-primary')
    continue_button.click()

    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '//*[@id="content"]/h1[contains(text(), "Your Account Has Been Created!")]')))
    except TimeoutException:
        warning = wait((By.CSS_SELECTOR, '#account-register > div.alert.alert-danger.alert-dismissible'), driver)
        assert warning.text == 'Warning: E-Mail Address is already registered!'
    driver.close()


def test_login_page(driver, url):
    driver.get(url=url)
    dropdown_register_login = driver.find_element(by=By.CSS_SELECTOR, value='#top-links > ul > li.dropdown')
    dropdown_register_login.click()
    login_ref = driver.find_element(by=By.CSS_SELECTOR, value='#top-links > ul > li.dropdown.open > ul > li:nth-child(2)')
    login_ref.click()

    left_part_head = wait((By.CSS_SELECTOR, '#content > div > div:nth-child(1) > div > h2'), driver)
    assert left_part_head.text == 'New Customer'

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
    driver.close()


def test_desktops_catalog(driver, url):
    driver.get(url=url)
    desktops_button = driver.find_element(by=By.CSS_SELECTOR, value='#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(1) > a')
    desktops_button.click()
    show_all_desktops_button = driver.find_element(by=By.CSS_SELECTOR, value='#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li.dropdown.open > div > a')
    show_all_desktops_button.click()
    refine_search = wait((By.CSS_SELECTOR, '#content > h3'), driver)
    assert refine_search.text == 'Refine Search'

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








driver_folder = r"C:\Users\marisarze\Downloads\browsers"
driver = webdriver.Chrome(executable_path=driver_folder+'/chromedriver.exe')
url = r"http://192.168.0.102:8081"
test_main(driver, url)

driver_folder = r"C:\Users\marisarze\Downloads\browsers"
driver = webdriver.Chrome(executable_path=driver_folder+'/chromedriver.exe')
url = r"http://192.168.0.102:8081"
test_iphone_page(driver, url)

driver_folder = r"C:\Users\marisarze\Downloads\browsers"
driver = webdriver.Chrome(executable_path=driver_folder+'/chromedriver.exe')
url = r"http://192.168.0.102:8081"
test_register_page(driver, url)

driver_folder = r"C:\Users\marisarze\Downloads\browsers"
driver = webdriver.Chrome(executable_path=driver_folder+'/chromedriver.exe')
url = r"http://192.168.0.102:8081"
test_login_page(driver, url)

driver_folder = r"C:\Users\marisarze\Downloads\browsers"
driver = webdriver.Chrome(executable_path=driver_folder+'/chromedriver.exe')
url = r"http://192.168.0.102:8081"
test_desktops_catalog(driver, url)