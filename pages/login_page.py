from  pages.base_page import BasePage

class LoginPage(BasePage):

    usernamefield = "#user-name"
    passwordfield = "#password"
    submit_button = "#login-button"


    def enter_username(self,username):
        self.page.locator(self.usernamefield).fill(username)

    def enter_password(self, password):
        self.page.locator(self.passwordfield).fill(password)


    def click_login(self):
        self.click(self.submit_button)


    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        self.page.wait_for_url("https://www.saucedemo.com/inventory.html")

    def get_valid_username(self):
        valid_username = self.page.locator("#login_credentials").inner_text().split("\n")[1]
        return valid_username

    def get_valid_password(self):
        valid_password = self.page.locator(".login_password").inner_text().split("\n")[1]
        return valid_password
