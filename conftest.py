import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.get("https://anatoly-karpovich.github.io/HiqoMeetup/")
    yield browser
    browser.close()
    browser.quit()

