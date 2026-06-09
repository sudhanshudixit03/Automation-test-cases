class LoginPage:

    def __init__(self, page):

        self.page = page

    def login(self, username, password):

        self.page.fill("#user-name", "standard_user")

        self.page.fill("#password", "secret_sauce")

        self.page.click("#login-button")





