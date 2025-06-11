from selenium.webdriver.common.by import By


class AutorisationLocators:
    LOGIN_BUTTON = By.XPATH, "//button[text()='Вход и регистрация']" # вход и регистпация
    LOGOUT_BUTTON = By.XPATH, "//button[text()='Выйти']"  # вход и регистпация
    NOT_ACCAUNT = By.XPATH, "//button[text()='Нет аккаунта']" # нет аккаунта
    CREATE_ACCAUNT = By.XPATH, "//button[text()='Создать аккаунт']" # создать аккаунт
    FIELD_EMAIL = By.NAME, "email" # поле email
    FIELD_PASS = By.NAME, "password" # ввод пароля
    FIELD_SUB_PASS = By.NAME, "submitPassword" # подтверждение пароля
    ERR_TEXT = By.CLASS_NAME, 'input_span__yWPqB' # сообщение об ошибке при логине
    USER_TXT = By.XPATH, "//h3[text()='User.']" # отображение салогиненного пользователя
    MAIN_LOGIN_BUTTON = By.XPATH, "//button[text()='Войти']" # кнопка выйти
    POST_ON = By.XPATH, "//button[text()='Разместить объявление']" # кнопка разместить объявление
    ERR_POST_ON = By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']" # сообщение о необходимости авторизоваться
    POST_NAME = By.NAME, "name" # название
    POST_DISCR = By.XPATH, "//textarea[@class='textarea_inputStandart__IoNxq spanGlobal']" # описание товара
    POST_PRICE = By.NAME, "price" # стоимость
    POST_CATEG_LIST = By.XPATH, "//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']" # список категорий
    POST_CATEG = By.XPATH, "//button[@class='dropDownMenu_btn__o8ARs dropDownMenu_noDefault__wSKsP']"  # категория
    POST_STATE_LIST = By.CLASS_NAME, "radioUnput_shell__Wtdwe"  # список состояний
    POST_CiTY_LIST = By.XPATH, "//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']"  # список городов
    POST_CITY = By.XPATH, "//button[@class='dropDownMenu_btn__o8ARs dropDownMenu_noDefault__wSKsP']"  # город
    POST_ON_MAIN = By.XPATH, "//button[text()='Опубликовать']"  # категория
    USER_PROFILE = By.XPATH, '//button[@class="circleSmall"]' # переход в профиль
    MY_POST = By.CLASS_NAME, "profile_profile__bixlA" # мои объявления
    EMAIL_BORDER = By.CLASS_NAME, 'input_inputError__fLUP9'
    USER_AVATAR = By.CLASS_NAME, 'svgSmall' # аватар профиля
    CHECK_POST_NAME = By.CLASS_NAME, 'picture' # наименование товара для проверки
    