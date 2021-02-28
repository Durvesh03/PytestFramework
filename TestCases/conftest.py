from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome('C:\\Users\\durve\\PycharmProjects\\chromedriver.exe')
        print("Launching Chrome Browser.....")
    elif browser == "edge":
        driver = webdriver.Edge('C:\\Users\\durve\\PycharmProjects\\msedgedriver.exe')
        print("Launching Edge Browser.....")
    else:
        driver = webdriver.Chrome('C:\\Users\\durve\\PycharmProjects\\chromedriver.exe')
        print("Launching Chrome Browser.....")
    return driver

def pytest_addoption(parser): #to get value from command line
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return value to setup
    return request.config.getoption("--browser")

################Pytest HTML report#####################

#It is hook for adding Environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Durvesh'

# It is hook for delete/modify Environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

