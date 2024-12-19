import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: '--browser_name=chrome' or '--browser_name=firefox'")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: '--language=en' or '--language=ru'")

@pytest.fixture(params=["chrome", "firefox"], scope="function")
def browser(request):
    browser_name = request.param
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        driver_browser = webdriver.Firefox(options=options)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
