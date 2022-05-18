import pytest
from selenium.webdriver.common.by import By
from locators import *
from data import *


# valid datas
@pytest.mark.parametrize("user", user)
@pytest.mark.parametrize("keys", keys)
def valid_registration(browser, userName, password):
    reg_btn = browser.find_element(*Buttons.first_reg_btn).click()
    name = browser.find_element(*Inputs.reg_name).send_keys(userName)
    pass_w = browser.find_element(*Inputs.reg_password).send_keys(password)
    r_btn = browser.find_element(*Buttons.sec_btn).click()


# invalid name
@pytest.mark.parametrize("user", invalid_usr)
@pytest.mark.parametrize("keys", invalid_psw)
def invalid_name_registration(browser, invalid_usr, invalid_psw):
    reg_btn = browser.find_element(*Buttons.first_reg_btn).click()
    name = browser.find_element(*Inputs.reg_name).send_keys(invalid_usr)
    pass_w = browser.find_element(*Inputs.reg_password).send_keys(invalid_psw)
    r_btn = browser.find_element(*Buttons.sec_btn).click()