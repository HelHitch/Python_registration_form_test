import pytest
from selenium.webdriver.common.by import By
from locators import Buttons
from data import *
from locators import *

@pytest.mark.parametrize("user", user)
@pytest.mark.parametrize("keys", keys)
def valid_log_in(browser, user, keys):
    input_password_submit = browser.find_element(*Inputs.log_in_name).send_keys(keys)
    input_name_submit = browser.find_element(*Inputs.log_in_password).send_keys(user)  # send password
    btn = browser.find_element(*Buttons.sub_btn).click()

@pytest.mark.parametrize("user", invalid_usr)
@pytest.mark.parametrize("keys", invalid_psw)
def invalid_name_log_in(browser, invalid_usr, invalid_psw):
    input_password_submit = browser.find_element(*Inputs.log_in_name).send_keys(invalid_psw)
    input_name_submit = browser.find_element(*Inputs.log_in_password).send_keys(invalid_usr)  # send password
    btn = browser.find_element(*Buttons.sub_btn).click()

