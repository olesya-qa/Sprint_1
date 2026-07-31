from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:
    ORDER_CARD = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]")
    ORDER_CARD_TITLE = (
        By.XPATH,
        "//li[contains(@class, 'OrderHistory_listItem')][1]//h2",
    )
    ORDER_NUMBER = (
        By.XPATH,
        "(//div[contains(@class, 'OrderHistory_textBox')]"
        "/p[contains(@class, 'text_type_digits-default')])[1]",
    )
    ORDER_FEED_LINK = (By.XPATH, "//p[text()='Лента Заказов']/ancestor::a")
