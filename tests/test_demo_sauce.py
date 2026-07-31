from playwright.sync_api import Page
from pages.cartpage import CartPage
from pages.chekout_page import Checkout
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_verify_sauce_login(page:Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = Checkout(page)

    page.goto("https://www.saucedemo.com/")

    login_page.login(login_page.get_valid_username() ,login_page.get_valid_password())
    inventory_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_product_to_cart("Sauce Labs Fleece Jacket")
    inventory_page.verify_product_count()

    cart_page.navigate_to_cart()
    cart_page.verify_product_count()
    cart_page.verify_item("Sauce Labs Bolt T-Shirt","Sauce Labs Fleece Jacket")
    cart_page.checkout()

    checkout_page.fill_checkout_info("Test","user","4110051")
    checkout_page.click_continue()

    checkout_page.get_product_price_before_tax()
    checkout_page.get_product_price_after_tax()

    assert checkout_page.get_product_price_after_tax() > checkout_page.get_product_price_before_tax(), (
        f"Total price  is not greater than item price "
    )

    checkout_page.finish()
    checkout_page.verify_thank_you_message()

