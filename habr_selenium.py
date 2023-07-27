from selenium import webdriver
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


driver = webdriver.Chrome()
print(driver, driver.caps["browserVersion"])
driver.get("https://habr.com/ru/all/")
articles = driver.find_element(By.CLASS_NAME, 'tm-articles-list')

parsed_data = []
all_element = articles.find_elements(By.CLASS_NAME, 'article')
for article in articles.find_elements(By.CLASS_NAME, 'article'):
    h2_element = article.find_element(By.TAG_NAME, 'h2')
    a_element = h2_element.find_element(By.TAG_NAME, 'a')
    span_element = a_element.find_element(By.TAG_NAME, 'span')
    time_element = wait_element(driver, by=By.TAG_NAME, value='time')

    title = span_element.text
    link = a_element.get_attribute('href')
    date_time = time_element.get_attribute('datetime')

    parsed_data.append({
        'title': title,
        'link': link,
        'datetime': date_time
    })

for item in parsed_data:
    driver.get(item['link'])
    article = wait_element(driver, by=By.ID, value='post-content-body')
    item['text'] = article.text

# pprint(parsed_data)
