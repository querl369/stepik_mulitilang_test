from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default=None, help='Choose language etc"es/ru/ua/fr/de..."')

@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        print(f"\nstart chrome browser for test.. with {user_language} language")
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        print(f"\nstart firefox browser for test.. with {user_language} language")
    else:
        raise pytest.UsageError("--user_language should be defined")
    yield browser
    print("\nquit browser..")
    browser.quit()