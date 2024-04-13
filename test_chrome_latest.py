import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

username = os.environ.get("SAUCE_USERNAME")
access_key = os.environ.get("SAUCE_ACCESS_KEY")


def check_version(options):
    driver = webdriver.Remote(command_executor="https://ondemand.us-west-1.saucelabs.com:443/wd/hub", options=options)
    print(f"Sauce Session: https://app.saucelabs.com/tests/"+driver.session_id)
    driver.get('chrome://version')
    print(f"Chrome version is: ", driver.capabilities['browserVersion'])
    driver.quit()

def test_chrome_version():
    options = ChromeOptions()
    options.browser_version = 'latest'
    options.platform_name = 'Windows 10'
    sauce_options = {}
    sauce_options['username'] = f'{username}'
    sauce_options['accessKey'] = f'{access_key}'
    sauce_options['build'] = 'Browser Version Check'
    sauce_options['name'] = 'Chrome Latest'
    options.set_capability('sauce:options', sauce_options)

    check_version(options)

test_chrome_version()
