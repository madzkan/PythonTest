import pytest


from appium import webdriver
from src.testproject.sdk import drivers, addons


def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

@pytest.fixture(scope="session")
def driver():
    capabilities = {
        "platformName": "Android",
        "udid": "emulator-5554",
        "appPackage": "com.india.bb.test",
        "autoAcceptAlerts": True,
        "autoGrantPermissions": True,
        "appActivity": "com.bbapp.MainActivity",
        "automationName": "UIautomator2"
    }

    driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=capabilities)

    return driver

def teardown():

    driver.quit()