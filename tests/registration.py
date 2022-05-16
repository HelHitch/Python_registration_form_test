import time

import allure
import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from allure_commons.types import AttachmentType


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.get("https://anatoly-karpovich.github.io/HiqoMeetup/")
    yield browser
    browser.quit()


invalid_passwords_datas = {
    'argnames': 'userName,password',
    'argvalues': [('Name', '1234567'), ('Name', 'aaaaaaaa'), ('Name', 'AAAAAAAA'), ('Name', 'AAAAaa1'),
                  ('Name', 'aaBc!678'), ('Name', ''), ('Name', '        ')]}

valid_datas = {
    'argnames': 'userName,password',
    'argvalues': [('lJHMswktSGGmVwZGQLUBnSgHEQgNItCyteMFLcpu', '123456Ab'), ('Name Arnold', '123456Ab'),
                  ('Name-Arnold', '26mICcCu'), ('Name', '26mIC Cu')]}

invalid_name_datas = {
    'argnames': 'userName,password',
    'argvalues': [('lJHMswktSGGmVwZGQLUBnSgHEQgNItCyteMFLcpu8745', '123456Ab'), ('0', '123456Ab'),
                  ('1234', '123456Ab'), ('Русяз', '123456Ab'), ('Select* FROM NAMES', '123456Ab'),
                  ('<i>name<i>', '123456Ab'), ('', '123456Ab'), ('qwertyuiopasdfghjklzxcvbnm', '123456Ab'),
                  ('Name.', '123456Ab'), ('________', '123456Ab'), (' Name ', '123456Ab')]}


class TestRegistration:

    @allure.feature("Проверяем невалидные пароли")
    @pytest.mark.xfail(raises=AssertionError)
    @pytest.mark.parametrize(**invalid_passwords_datas)
    def test_invalid_password(self, browser, userName, password):
        reg_btn = browser.find_element(By.ID, "registerOnLogin").click()
        name = browser.find_element(By.ID, 'userNameOnRegister').send_keys(userName)
        password = browser.find_element(By.ID, 'passwordOnRegister').send_keys(password)
        btn = browser.find_element(By.ID, "register").click()
        WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.ID, "errorMessageOnRegister")))
        message = browser.find_element(By.ID, "errorMessageOnRegister")
        print("", message.text, sep="\n")
        with allure.step("Проверяем, что в ошибке упоминается пароль"):
            assert "password", "Password" in message.text
        with allure.step("Проверяем, что регистрация не проходит успешно"):
            assert message.text != "Successfully registered! Please, click Back to return on login page", "Регистрация не должна" \
                                                                                                          " проходить успешно"


    @pytest.mark.xfail(raises=AssertionError)
    @pytest.mark.parametrize(**invalid_name_datas)
    def test_invalid_name(self, browser, userName, password):
        reg_btn = browser.find_element(By.ID, "registerOnLogin").click()
        name = browser.find_element(By.ID, 'userNameOnRegister').send_keys(userName)
        password = browser.find_element(By.ID, 'passwordOnRegister').send_keys(password)
        btn = browser.find_element(By.ID, "register").click()
        WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.ID, "errorMessageOnRegister")))
        message = browser.find_element(By.ID, "errorMessageOnRegister")
        print("", message.text, sep="\n")
        with allure.step("Проверяем, что в ошибке упоминается username"):
            assert "username", "User" in message.text
        assert message.text != "Successfully registered! Please, click Back to return on login page"

    @pytest.mark.parametrize(**invalid_name_datas)
    def test_valid_datas(self, browser, userName, password):
        reg_btn = browser.find_element(By.ID, "registerOnLogin").click()  #click at Registration btn
        name = browser.find_element(By.ID, 'userNameOnRegister').send_keys(userName) #send uername
        password = browser.find_element(By.ID, 'passwordOnRegister').send_keys(password) #send password
        btn = browser.find_element(By.ID, "register").click() #refister account
        message = browser.find_element(By.ID, "errorMessageOnRegister") #check presence of error message
        print("", message.text, sep="\n") # print the message
        assert "username", "User" in message.text # check that the message is about username
        assert message.text == "Successfully registered! Please, click Back to return on login page"
        time.sleep(3)
        # assert that registration went successful
        btn_back = browser.find_element(By.ID, "backOnRegister").click() #moving to login page
        #time.sleep(5)
        input_password_submit = browser.find_element(By.ID, "password").send_keys(password)
        input_name_submit = browser.find_element(By.ID, "userName").send_keys(userName) #send password
        btn = browser.find_element(By.ID, "submit").click()
        WebDriverWait(browser,2).until(EC.visibility_of_element_located((By.ID, "errorMessage")))
        message = browser.find_element(By.ID, "errorMessage")
        print(message.text)
