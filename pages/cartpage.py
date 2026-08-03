from pages.base_page import BasePage
from  playwright.sync_api import  Page ,expect

class CartPage(BasePage):

    shopping_cart_link = '[data-test="shopping-cart-link"]'
    cart_item = "[class='cart_item']"
    inventory_items = '[class="inventory_item_name"]'
    checkout_button = "#checkout"


    def navigate_to_cart(self):
        self.page.locator(self.shopping_cart_link).click()

    def verify_product_count(self):
       items =  self.page.locator(self.cart_item)
       expect(items).to_have_count(2)


    def verify_item(self,prod1,prod2):

           product1 = self.page.locator(self.inventory_items).nth(0)
           product2 = self.page.locator(self.inventory_items).nth(1)

           expect(product1).to_be_visible()
           expect(product2).to_be_visible()

           expect(product1).to_contain_text(prod1)
           expect(product2).to_contain_text(prod2)


    def checkout(self):
        self.page.locator(self.checkout_button).click()

        


