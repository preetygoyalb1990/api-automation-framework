class LoginPage:

    def __init__(self, page):
        self.page = page

    def open_login_page(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def enter_username(self, username):
        self.page.fill("#username", username)

    def enter_password(self, password):
        self.page.fill("#password", password)

    def click_login(self):
        self.page.click("button[type='submit']")

    def get_heading(self):
        return self.page.locator("h2").text_content()
    def get_error_message(self):  # if move last 2lines then failed
      return self.page.locator("#flash").text_content()