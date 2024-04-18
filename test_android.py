import os
import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.appium_service import AppiumService

url = "https://ondemand.us-west-1.saucelabs.com:443/wd/hub"

@pytest.fixture(scope="module")
def driver():
    capabilities = {}
    capabilities['appium:deviceName'] = 'Google.*'
    capabilities['platformName'] = 'Android'
    capabilities['browserName'] = 'Chrome'
    capabilities['sauce:options'] = {}
    capabilities['sauce:options']['build'] = 'Android RDC SO'
    capabilities['sauce:options']['name'] = 'Android Chrome Test'
    capabilities['sauce:options']['username'] = os.environ.get("SAUCE_USERNAME")
    capabilities['sauce:options']['accessKey'] = os.environ.get("SAUCE_ACCESS_KEY")
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(capabilities))
    yield driver
    driver.quit()

def test_android(driver):
    print(f"Sauce Session: https://app.saucelabs.com/tests/{driver.session_id}")
    driver.get('https://android.com')