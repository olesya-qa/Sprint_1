from selenium.webdriver.common.by import By


class FeedPageLocators:
    FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    ORDERS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]")
    FIRST_ORDER_CARD = (
        By.XPATH,
        "//li[contains(@class, 'OrderHistory_listItem')][1]",
    )
    ORDER_MODAL = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]"
        "//div[contains(@class, 'Modal_orderBox') or contains(@class, 'Modal_modal__contentBox')]",
    )
    ORDER_MODAL_TITLE = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//h2",
    )
    TOTAL_COMPLETED_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p",
    )
    TODAY_COMPLETED_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p",
    )
    FEED_ORDER_NUMBERS = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_list')]"
        "//p[contains(@class, 'text_type_digits-default')]",
    )
    IN_PROGRESS_ORDER_NUMBERS = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderListReady')]"
        "/li[contains(@class, 'text_type_digits-default')]",
    )
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']/ancestor::a")
