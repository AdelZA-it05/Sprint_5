from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from faker import Faker
from locators import AutorisationLocators
import data
import pytest


faker = Faker()

class TestDoskaCreateUser:

    @pytest.mark.parametrize(
        'test_login, test_pass, n_case',
        [
            [faker.ascii_free_email(), faker.password(), 1]
          , [faker.text(15), faker.password(), 2]
          , ['exist_user', 'exist_pass', 3]
        ]
    )
    def test_create_login(self, driver, create_user, test_login, test_pass, n_case):
        try:
            driver.get(data.web_link)
            # вход и регистрация
            driver.find_element(*AutorisationLocators.LOGIN_BUTTON).click()
            # нет аккаунта
            WebDriverWait(driver, 11).until(expected_conditions.visibility_of_element_located(
                (AutorisationLocators.NOT_ACCAUNT)))
            driver.find_element(*AutorisationLocators.NOT_ACCAUNT).click()

            # ввод логина и пароля
            if n_case == 3:
                test_login = create_user[0]
                test_pass = create_user[1]
            driver.find_element(*AutorisationLocators.FIELD_EMAIL).send_keys(test_login)
            driver.find_element(*AutorisationLocators.FIELD_PASS).send_keys(test_pass)
            driver.find_element(*AutorisationLocators.FIELD_SUB_PASS).send_keys(test_pass)
            # создать аккаунт
            driver.find_element(*AutorisationLocators.CREATE_ACCAUNT).click()

            # Проверки по кейсам
            if n_case == 1:
                # возврат на главную страницу
                WebDriverWait(driver, 11).until(expected_conditions.visibility_of_element_located(
                    (AutorisationLocators.USER_TXT)))

                # Текст 'User.'
                st1 = driver.find_element(*AutorisationLocators.USER_TXT).text
                assert st1 == 'User.'
            elif n_case == 2:
                WebDriverWait(driver, 11).until(expected_conditions.visibility_of_element_located(
                    (AutorisationLocators.ERR_TEXT)))

                #  Текст Ошибка красным
                st2 = driver.find_element(*AutorisationLocators.EMAIL_BORDER).value_of_css_property('border')
                assert driver.find_element(
                    *AutorisationLocators.ERR_TEXT).text == 'Ошибка' and st2 == '1px solid rgb(255, 105, 114)'
            elif n_case == 3:
                WebDriverWait(driver, 11).until(expected_conditions.visibility_of_element_located(
                    (AutorisationLocators.ERR_TEXT)))
                assert driver.find_element(*AutorisationLocators.ERR_TEXT).text == 'Ошибка'
        finally:
            pass

