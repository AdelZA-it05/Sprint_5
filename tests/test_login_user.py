from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from faker import Faker
from locators import AutorisationLocators
import data
import pytest


faker = Faker()

class TestDoskaLoginUser:

    @pytest.mark.parametrize(
        'test_inout, n_case',
        [
            ['login', 1]
          , ['logout', 2]
        ]
    )
    def test_login_user(self, driver, create_user, test_inout, n_case):
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

            if n_case == 1:
                # поиск 'User.'
                WebDriverWait(driver, 11).until(expected_conditions.visibility_of_element_located(
                    (AutorisationLocators.USER_TXT)))
                st1 = driver.find_element(*AutorisationLocators.USER_TXT).text
                st3 = driver.find_element(*AutorisationLocators.USER_AVATAR).get_attribute('xmlns')
                assert st1 == 'User.' and st3 == 'http://www.w3.org/2000/svg'

            elif n_case == 2:
                # выйти
                WebDriverWait(driver, 11).until(expected_conditions.visibility_of_element_located(
                    (AutorisationLocators.LOGOUT_BUTTON)))
                driver.find_element(*AutorisationLocators.LOGOUT_BUTTON).click()

                # поиск 'Разместить объявление'
                st2 = driver.find_element(*AutorisationLocators.POST_ON).text
                assert st2 == 'Разместить объявление'



        finally:
            pass

