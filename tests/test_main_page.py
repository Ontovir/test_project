import pytest
import allure
from pages.main_page import MainPage

@allure.feature("Главная страница")
@pytest.mark.parametrize("section, expected_url", [
    ("click_about_us", "https://effective-mobile.ru/about"),
    ("click_contacts", "https://effective-mobile.ru/contacts")
])
def test_navigation(page, section, expected_url):
    main_page = MainPage(page)
    main_page.open("https://effective-mobile.ru/")
    getattr(main_page, section)()  # Вызываем метод по имени
    assert main_page.get_current_url() == expected_url, f"URL должен быть {expected_url}"