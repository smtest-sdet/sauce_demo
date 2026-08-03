from playwright.sync_api import expect

from pages.base_page import BasePage

class Checkout(BasePage):
    first_name_input = "#first-name"
    last_name_input = "#last-name"
    postal_code_input = "#postal-code"
    continue_button = "#continue"
    finish_button = "#finish"
    sub_total_label = ".summary_subtotal_label"
    summary_total_label = ".summary_total_label"

    def fill_checkout_info(self,first_name,last_name,postal_code):
        expect(self.page.locator(self.first_name_input)).to_be_visible()
        self.page.locator(self.first_name_input).fill(first_name)
        self.page.locator(self.last_name_input).fill(last_name)
        self.page.locator(self.postal_code_input).fill(postal_code)

    def click_continue(self):
        self.page.locator(self.continue_button).click()

    def get_product_price_before_tax(self):
        self.page.locator(self.finish_button).scroll_into_view_if_needed()
        price = self.page.locator(self.sub_total_label).inner_text().split("\n")[0]
        beforeprice = float(price.replace("Item total: $", ""))
        print(beforeprice)
        return beforeprice


    def get_product_price_after_tax(self):
        self.page.locator(self.finish_button).scroll_into_view_if_needed()
        total = self.page.locator(self.summary_total_label).inner_text().split("\n")[0]
        afterprice =float(total.replace("Total: $", ""))
        print(afterprice)
        return afterprice

    def finish(self):
        self.page.locator(self.finish_button).click()

    def verify_thank_you_message(self):
        expect(self.page.get_by_text("Thank you for your order!")).to_be_visible()


