from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.timeout = timeout

    def open(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_elements(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_invisible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_until(self, condition):
        return WebDriverWait(self.driver, self.timeout).until(condition)

    def get_text(self, locator):
        return self.find_element(locator).text

    def click(self, locator):
        element = self.wait_for_clickable(locator)
        self.scroll_to(element)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script('arguments[0].click();', element)

    def type_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def scroll_to(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )

    def drag_and_drop(self, source_locator, target_locator, counter_locator=None):
        """HTML5 drag-and-drop: ActionChains, при неудаче — JS (нужен Firefox)."""
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        counter_before = self.get_text(counter_locator) if counter_locator else None

        ActionChains(self.driver).drag_and_drop(source, target).perform()

        if counter_locator:
            counter_after = self.get_text(counter_locator)
            if counter_after != counter_before and counter_after != '0':
                return

        # В Firefox нативный drag-and-drop для HTML5 часто не срабатывает
        script = """
        const source = arguments[0];
        const target = arguments[1];
        const dataTransfer = {
            data: {},
            setData: function(key, value) { this.data[key] = value; },
            getData: function(key) { return this.data[key]; },
            dropEffect: 'move',
            effectAllowed: 'move'
        };
        function fire(element, type) {
            const event = new Event(type, { bubbles: true, cancelable: true });
            Object.defineProperty(event, 'dataTransfer', { value: dataTransfer });
            element.dispatchEvent(event);
        }
        fire(source, 'dragstart');
        fire(target, 'dragenter');
        fire(target, 'dragover');
        fire(target, 'drop');
        fire(source, 'dragend');
        """
        self.driver.execute_script(script, source, target)
