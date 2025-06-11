from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import AutorisationLocators
import data


class TestPostDoskaNotAauthorizedUser:

    def test_post_not_authorized_user(self, driver):
        try:
            driver.get(data.web_link)
            # разместить объявление
            driver.find_element(*AutorisationLocators.POST_ON).click()

            WebDriverWait(driver, 25).until(expected_conditions.visibility_of_element_located(
                (AutorisationLocators.ERR_POST_ON)))

            # проверка
            st2 = driver.find_element(*AutorisationLocators.ERR_POST_ON).text
            assert st2 == 'Чтобы разместить объявление, авторизуйтесь'
        finally:
            pass