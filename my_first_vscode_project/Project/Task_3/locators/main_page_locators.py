from selenium.webdriver.common.by import By


class MainPageLocators:
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']/ancestor::a")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']/ancestor::a")
    ORDER_FEED_LINK = (By.XPATH, "//p[text()='Лента Заказов']/ancestor::a")
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    INGREDIENT_BUN = (
        By.XPATH,
        "//p[text()='Флюоресцентная булка R2-D3']/parent::a",
    )
    INGREDIENT_BUN_COUNTER = (
        By.XPATH,
        "//p[text()='Флюоресцентная булка R2-D3']/parent::a"
        "//p[contains(@class, 'counter')]",
    )
    CONSTRUCTOR_BASKET = (
        By.XPATH,
        "//section[contains(@class, 'BurgerConstructor_basket')]",
    )
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    INGREDIENT_MODAL = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]",
    )
    INGREDIENT_MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]"
        "//button[contains(@class, 'Modal_modal__close')]",
    )
    ORDER_NUMBER = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//h2",
    )
    ORDER_ID_HINT = (By.XPATH, "//p[text()='идентификатор заказа']")
    ORDER_LOADING_NUMBER = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//h2[text()='9999']",
    )
