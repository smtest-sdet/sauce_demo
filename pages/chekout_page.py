from playwright.sync_api import expect

from pages.base_page import BasePage

class Checkout(BasePage):

    def fill_checkout_info(self,first_name,last_name,postal_code):
        expect(self.page.locator("#first-name")).to_be_visible()
        self.page.locator("#first-name").fill(first_name)
        self.page.locator("#last-name").fill(last_name)
        self.page.locator("#postal-code").fill(postal_code)

    def click_continue(self):
        self.page.locator("#continue").click()

    def get_product_price_before_tax(self):
        self.page.locator("#finish").scroll_into_view_if_needed()
        price = self.page.locator('.summary_subtotal_label').inner_text().split("\n")[0]
        beforeprice = float(price.replace("Item total: $", ""))
        print(beforeprice)
        return beforeprice


    def get_product_price_after_tax(self):
        self.page.locator("#finish").scroll_into_view_if_needed()
        total = self.page.locator(".summary_total_label").inner_text().split("\n")[0]
        afterprice =float(total.replace("Total: $", ""))
        print(afterprice)
        return afterprice

    def finish(self):
        self.page.locator("#finish").click()

    def verify_thank_you_message(self):
        expect(self.page.get_by_text("Thank you for your order!")).to_be_visible()


