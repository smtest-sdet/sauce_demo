from _pyrepl import pager

from playwright.sync_api import  Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self,locator):
        self.page.locator(locator).click()

    def fill(self,locator,value):
        self.page.locator(locator).fill(value)

    def get_text(self,locator):
        return self.page.locator(locator).inner_text()

