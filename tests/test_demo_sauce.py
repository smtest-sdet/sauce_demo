from playwright.sync_api import Page
from pages.cartpage import CartPage
from pages.chekout_page import Checkout
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import  json

with open("testdata/sauce_demo_data.json", "r") as file:
    testdata = json.load(file)

def test_verify_sauce_login(page:Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = Checkout(page)

    page.goto(testdata["base_url"])

    login_page.login(login_page.get_valid_username() ,login_page.get_valid_password())
    inventory_page.add_product_to_cart(testdata["product1"])
    inventory_page.add_product_to_cart(testdata["product2"])
    inventory_page.verify_product_count()

    cart_page.navigate_to_cart()
    cart_page.verify_product_count()
    cart_page.verify_item(testdata["product1"],testdata["product2"])
    cart_page.checkout()

    checkout_page.fill_checkout_info( testdata["first_name"],testdata["last_name"],testdata["postal_code"])
    checkout_page.click_continue()

    checkout_page.get_product_price_before_tax()
    checkout_page.get_product_price_after_tax()

    assert checkout_page.get_product_price_after_tax() > checkout_page.get_product_price_before_tax(), (
        testdata["not_equal_msg"]
    )

    checkout_page.finish()
    checkout_page.verify_thank_you_message()

