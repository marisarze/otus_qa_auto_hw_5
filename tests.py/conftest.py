import pytest
import os
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru", help ="url for tests")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "mozilla", "edge"], help="browser driver where tests runs in")
    parser.addoption("--driver-folder", action="store", default="~/Downloads", help="folder which contains driver for browser")


@pytest.fixture
def browser(request):
    browser_type = request.config.getoption("--browser")
    driver_folder = request.config.getoption("--driver-folder")
    if browser_type == 'chrome':
        target = webdriver.Chrome(executable_path=os.path.expanduser(driver_folder))
    elif browser_type == 'mozilla':
        target = webdriver.Firefox(executable_path=os.path.expanduser(driver_folder))
    elif browser_type == 'edge':
        target = webdriver.Edge(executable_path=os.path.expanduser(driver_folder))
    else:
        raise ValueError(f"Browser {browser_type} is not supported.")
    yield target

