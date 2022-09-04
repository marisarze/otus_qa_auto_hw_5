import pytest
import os
from selenium import webdriver
from sys import platform
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru", help ="url for tests")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "mozilla", "edge"], help="browser driver where tests runs in")
    parser.addoption("--driver_folder", action="store", default="~/Downloads", help="folder which contains driver for browser")
    parser.addoption("--headless", action="store_true", default="false", help="set headless property to browser")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def driver(request):
    extension = ''
    if platform in ['win32', 'win64']: extension='.exe'
    browser_type = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver_folder = os.path.expanduser(request.config.getoption("--driver_folder"))
    if browser_type == 'chrome':
        if headless:
            options = webdriver.ChromeOptions()
            options.headless = True
        target = webdriver.Chrome(executable_path=driver_folder+'/chromedriver'+extension, options=options)
    elif browser_type == 'mozilla':
        if headless:
            options = webdriver.FirefoxOptions()
            options.headless = True
        target = webdriver.Firefox(executable_path=driver_folder+'/mozilla'+extension, options=options)
    elif browser_type == 'edge':
        target = webdriver.Edge(executable_path=driver_folder+'/edgedriver'+extension)
    else:
        raise ValueError(f"Browser {browser_type} is not supported.")
    yield target
    target.close()


# driver_folder = r"C:\Users\marisarze\Downloads\browsers"
# driver = webdriver.Chrome(executable_path=driver_folder+'/chromedriver.exe')
# url = r"http://192.168.0.102:8081"
# test_main(driver, url)

# driver_folder = r"C:\Users\marisarze\Downloads\browsers"
# driver = webdriver.Chrome(executable_path=driver_folder+'/chromedriver.exe')
# url = r"http://192.168.0.102:8081"
# test_iphone_page(driver, url)

# driver_folder = r"C:\Users\marisarze\Downloads\browsers"
# driver = webdriver.Chrome(executable_path=driver_folder+'/chromedriver.exe')
# url = r"http://192.168.0.102:8081"
# test_register_page(driver, url)

# driver_folder = r"C:\Users\marisarze\Downloads\browsers"
# driver = webdriver.Chrome(executable_path=driver_folder+'/chromedriver.exe')
# url = r"http://192.168.0.102:8081"
# test_login_page(driver, url)

# driver_folder = r"C:\Users\marisarze\Downloads\browsers"
# driver = webdriver.Chrome(executable_path=driver_folder+'/chromedriver.exe')
# url = r"http://192.168.0.102:8081"
# test_desktops_catalog(driver, url)
