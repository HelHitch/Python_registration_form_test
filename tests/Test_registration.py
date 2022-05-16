import time
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests import Login_page
from locators import Buttons
import Reg_page
from data import *

Successfully_registered = "Successfully registered! Please, click Back to return on login page"

invalid_passwords_datas = {
    'argnames': 'userName,password',
    'argvalues': [('Name', '1234567'), ('Name', 'aaaaaaaa'), ('Name', 'AAAAAAAA'), ('Name', 'AAAAaa1'),
                  ('Name', 'aaBc!678'), ('Name', ''), ('Name', '        ')]}


class TestRegistration:

    @pytest.mark.parametrize("user", user)
    @pytest.mark.parametrize("keys", keys)
    def test_valid_datas(self, browser, user, keys):
        Reg_page.valid_registration(browser, user, keys)
        message = browser.find_element(By.ID, "errorMessageOnRegister")
        print("", message.text, sep="\n")
        assert "username", "User" in message.text
        assert message.text == "Successfully registered! Please, click Back to return on login page"
        btn_back = browser.find_element(*Buttons.back_btn).click()  # moving to login page
        Login_page.valid_log_in(browser, user, keys)
        msg = browser.find_element(By.ID, "successMessage")
        assert "Hello" in msg.text, "что-то пошло не так..."
        print(msg.text)


    @pytest.mark.parametrize("invaild_user", invalid_usr)
    @pytest.mark.parametrize("invalid_keys", invalid_psw)
    def test_invalid_name(self, browser, invaild_user, invalid_keys):
        Reg_page.invalid_name_registration(browser, invaild_user, invalid_keys)  # форма регистрации
        message = browser.find_element(By.ID, "errorMessageOnRegister")  # находим сообщение системе о данных
        print("", message.text, sep="\n")  # выводим сообщение, хотя может просто добавлю проверку на отсутствие саксеса
        assert "username", "User" in message.text  # проверяем, что ошибка указывает на невалидные данные
        assert message.text != Successfully_registered, "Такое имя не должно приниматься системой"  # проверяем, что сообщеие не содержит саксеса
    # я три часа пыталась реализовать функцию, которая будет продолжать тестирование. То есть:
    # перейдет на форму логина и провери войдет ли он под данными, которые признал невалидными
    #пробовала и иф и трай эксепт, херня какая то

