import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from faker import Faker
from locators import AutorisationLocators


import data
faker = Faker()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def create_user(driver, new_login = None, new_pass = None):
    try:
        if not new_login: new_login = faker.email()
        if not new_pass: new_pass = faker.password()
        driver.get(data.web_link)
        # вход и регистрация
        driver.find_element(*AutorisationLocators.LOGIN_BUTTON).click()
        # нет аккаунта
        WebDriverWait(driver, 11).until(expected_conditions.visibility_of_element_located(
            (AutorisationLocators.NOT_ACCAUNT)))
        driver.find_element(*AutorisationLocators.NOT_ACCAUNT).click()
        # ввод логина и пароля
        driver.find_element(*AutorisationLocators.FIELD_EMAIL).send_keys(new_login)
        driver.find_element(*AutorisationLocators.FIELD_PASS).send_keys(new_pass)
        driver.find_element(*AutorisationLocators.FIELD_SUB_PASS).send_keys(new_pass)
        # создать аккаунт
        driver.find_element(*AutorisationLocators.CREATE_ACCAUNT).click()
        # возврат на главную страницу (удалить)
        # WebDriverWait(driver, 11).until(expected_conditions.visibility_of_element_located(
        #    (AutorisationLocators.USER_TXT)))
        # # поиск 'User.'
        # st1 = driver.find_element(*AutorisationLocators.USER_TXT).text
        # assert st1 == 'User.'
        create_user = [new_login, new_pass]
    finally:
        pass
    return create_user

@pytest.fixture
def create_post(driver, create_user):
    try:
        driver.get(data.web_link)
        # вход и регистрация
        driver.find_element(*AutorisationLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 11).until(expected_conditions.visibility_of_element_located(
            (AutorisationLocators.FIELD_EMAIL)))

        # войти
        driver.find_element(*AutorisationLocators.FIELD_EMAIL).send_keys(create_user[0])
        driver.find_element(*AutorisationLocators.FIELD_PASS).send_keys(create_user[1])
        driver.find_element(*AutorisationLocators.MAIN_LOGIN_BUTTON).click()

        WebDriverWait(driver, 11).until(expected_conditions.visibility_of_element_located(
            (AutorisationLocators.USER_TXT)))

        # разместить объявление
        driver.find_element(*AutorisationLocators.POST_ON).click()

        # наименование
        new_name = faker.text(15)
        driver.find_element(*AutorisationLocators.POST_NAME).send_keys(new_name)

        # описание товара
        new_discr = faker.text(45)
        driver.find_element(*AutorisationLocators.POST_DISCR).send_keys(new_discr)

        # стоимость изменить на faker.pydecimal(7, 2, )
        driver.find_element(*AutorisationLocators.POST_PRICE).send_keys(11111, 11)

        # категория
        driver.find_element(*AutorisationLocators.POST_CATEG_LIST).click()

        # авто
        WebDriverWait(driver, 11).until(expected_conditions.visibility_of_element_located(
            (AutorisationLocators.POST_CATEG)))
        driver.find_element(*AutorisationLocators.POST_CATEG).click()

        # состояние товара новый
        driver.find_element(*AutorisationLocators.POST_STATE_LIST).click()

        # город
        driver.find_element(*AutorisationLocators.POST_CiTY_LIST).click()

        # москва
        WebDriverWait(driver, 11).until(expected_conditions.visibility_of_element_located(
            (AutorisationLocators.POST_CITY)))
        driver.find_element(*AutorisationLocators.POST_CITY).click()

        # опубликовать
        WebDriverWait(driver, 11).until(expected_conditions.visibility_of_element_located(
            (AutorisationLocators.POST_ON_MAIN)))
        driver.find_element(*AutorisationLocators.POST_ON_MAIN).click()

        # не понятно почему тут без таймслип не работает (разобраться)


        # профиль пользователя
        WebDriverWait(driver, 11).until(expected_conditions.visibility_of_element_located(
            (AutorisationLocators.USER_PROFILE)))
        driver.find_element(*AutorisationLocators.USER_PROFILE).click()

        # мои объявления наименование товара == new_name
        WebDriverWait(driver, 11).until(expected_conditions.visibility_of_element_located(
            (AutorisationLocators.MY_POST)))

        # проверка
        create_post = [driver.find_element(*AutorisationLocators.CHECK_POST_NAME).get_attribute('alt'), create_user]

    finally:
        pass
    return create_post




