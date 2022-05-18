from selenium.webdriver.common.by import By


class Buttons:
    first_reg_btn = (By.ID, "registerOnLogin")
    sec_btn = (By.ID, "register")
    back_btn = (By.ID, "backOnRegister")
    sub_btn = (By.ID, "submit")


class Inputs:
    reg_name = (By.ID, 'userNameOnRegister')
    reg_password = (By.ID, 'passwordOnRegister')
    log_in_name = (By.ID, "password")
    log_in_password = (By.ID, "userName")
