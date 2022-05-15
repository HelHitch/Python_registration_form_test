import time

import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.get("https://anatoly-karpovich.github.io/HiqoMeetup/")
    yield browser
    browser.quit()


invalid_passwords_datas = {
    'argnames': 'userName,password',
    'argvalues': [('Name', '1234567'), ('Name', 'aaaaaaaa'), ('Name', 'AAAAAAAA'), ('Name', 'AAAAaa1'), ('Name', 'aaBc!678'), ('Name', '')]}

invalid_name_datas = {
    'argnames': 'userName,password',
    'argvalues': [('0', '123456Ab'), ('1234', '123456Ab'), ('Русяз', '123456Ab'), ('Select* FROM NAMES', '123456Ab'), ('<i>name<i>', '123456Ab'),
                  ('', '123456Ab'), ('qwertyuiopasdfghjklzxcvbnm', '123456Ab'), ('Name.', '123456Ab')]}


class TestRegistration:

    @pytest.mark.parametrize(**invalid_passwords_datas)
    def test_invalid_password(self, browser, userName, password):
        reg_btn = browser.find_element(By.ID, "registerOnLogin").click()
        name = browser.find_element(By.ID, 'userNameOnRegister').send_keys(userName)
        password = browser.find_element(By.ID, 'passwordOnRegister').send_keys(password)
        btn = browser.find_element(By.ID, "register").click()
        WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.ID, "errorMessageOnRegister")))
        message = browser.find_element(By.ID, "errorMessageOnRegister")
        assert message.text != "Successfully registered! Please, click Back to return on login page", "Регистрация не должна" \
                                                                                                      " проходить успешно"

    @pytest.mark.parametrize(**invalid_name_datas)
    def test_invalid_name(self, browser, userName, password):
        reg_btn = browser.find_element(By.ID, "registerOnLogin").click()
        name = browser.find_element(By.ID, 'userNameOnRegister').send_keys(userName)
        password = browser.find_element(By.ID, 'passwordOnRegister').send_keys(password)
        btn = browser.find_element(By.ID, "register").click()
        WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.ID, "errorMessageOnRegister")))
        message = browser.find_element(By.ID, "errorMessageOnRegister")
        assert message.text != "Successfully registered! Please, click Back to return on login page", "Регистрация не должна" \
                                                                                                      " проходить успешно"