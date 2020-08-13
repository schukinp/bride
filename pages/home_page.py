from selene.api import *

# locators
login_btn = s('.login')
login_int = s('#auth-login')
password_int = s('#auth-password')
enter_now_btn = ss('.reg-btn')[1]
error = s('#login-err')
close_icon = s('.close')
popup_title = s('#content-auth > .title')

# class for home page methods
class HomePage():
    def login_as(self, username, password):
        login_btn.click()
        popup_title.should(have.text('Members log in here'))
        login_int.set(username)
        password_int.set(password)
        enter_now_btn.click()

    def check_login_error_is(self, error_text):
        error.should(have.text(error_text))

    def close_popup(self):
        close_icon.click()
