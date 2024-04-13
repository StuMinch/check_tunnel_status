import os
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

url = "https://ondemand.us-west-1.saucelabs.com:443/wd/hub"


def check_version(capabilities):
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(capabilities))
    driver.get('https://android.com')
    driver.quit()

def test_chrome_version():
    capabilities = {}
    capabilities['appium:deviceName'] = 'Google.*'
    capabilities['platformName'] = 'Android'
    capabilities['browserName'] = 'Chrome'
    capabilities['sauce:options'] = {}
    capabilities['sauce:options']['build'] = 'Android RDC SO'
    capabilities['sauce:options']['name'] = 'Android Chrome Test'
    capabilities['sauce:options']['username'] = os.environ.get("SAUCE_USERNAME")
    capabilities['sauce:options']['accessKey'] = os.environ.get("SAUCE_ACCESS_KEY")
    check_version(capabilities)

test_chrome_version()

