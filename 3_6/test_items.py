import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_check_button_exists(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    button = None
    try:
        button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        print("присутствует кнопка добавления в корзину")
    except NoSuchElementException:
        print("отсутствует кнопка добавления в корзину")

    # без строчки ниже тест выглядит лучше, и её можно просто стереть, но задание требует именно наличие Assert'а
    assert button is not None, 'дублирую текст отсутствия кнопки, чтобы было именно assert'