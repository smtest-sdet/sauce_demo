
from pages.base_page import BasePage

class InventoryPage(BasePage):

    def add_product_to_cart(self, product_name):
        self.page.locator(
            f"//*[text()='{product_name}']//following::button[1]"
        ).click()

    def verify_product_count(self):
        cart = self.page.locator("[data-test='shopping-cart-badge']")
        count = cart.inner_text()

        print(count)


    def navigate_to_cart(self):
        self.page.locator("[data-test='shopping-cart-link']").click()



