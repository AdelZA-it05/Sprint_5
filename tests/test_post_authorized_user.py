from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from faker import Faker
from locators import AutorisationLocators
import data
import time


faker = Faker()

class TestPostDoskaAuthorizedUser:

    def test_post_authorized_user(self, driver, create_user):
        try:
            driver.get(data.web_link)

            # вход и регистрация
            driver.find_element(*AutorisationLocators.LOGIN_BUTTON).click()

            WebDriverWait(driver, 11).until(expected_conditions.visibility_of_element_located(
                (AutorisationLocators.FIELD_EMAIL)))

            # логин под фикстурой create_user
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
            driver.find_element(*AutorisationLocators.POST_PRICE).send_keys(11111,11)

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
            time.sleep(1)

            # профиль пользователя
            WebDriverWait(driver, 11).until(expected_conditions.visibility_of_element_located(
                (AutorisationLocators.USER_PROFILE)))
            driver.find_element(*AutorisationLocators.USER_PROFILE).click()

            # мои объявления наименование товара == new_name
            WebDriverWait(driver, 11).until(expected_conditions.visibility_of_element_located(
                (AutorisationLocators.MY_POST)))

            # проверка
            st1 = driver.find_element(*AutorisationLocators.CHECK_POST_NAME).get_attribute('alt')
            assert st1 == new_name
        finally:
            pass
