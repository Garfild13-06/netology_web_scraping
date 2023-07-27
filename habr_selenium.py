from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def wait_element(driver, delay_seconds=1, by=By.TAG_NAME, value=None):
    """
    Иногда элементы на странице не пргружаются сразу
    Функция ждёт delay_seconds если элемент не пргрузился
    Если за отведённое время элемент не прогружается выбрасывается timeoutException
    :param driver: driver
    :param delay_seconds: маскимальное время ожидания
    :param by: поле поиска
    :param value: значение поиска
    :return: найденный элемент
    """

    return WebDriverWait(driver, delay_seconds).until(
        expected_conditions.presence_of_element_located((by, value))
    )


# service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome()
url = "https://habr.com/ru/all/"
driver.get(url)
print(driver)
