from pages.base_page import BasePage
from playwright.sync_api import Page

class MainPage(BasePage):
    ABOUT_US = "text=О нас"
    CONTACTS = "text=Контакты"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def click_about_us(self):
        self.page.click(self.ABOUT_US)

    def click_contacts(self):
        self.page.click(self.CONTACTS)

    def get_current_url(self):
        return self.page.url
