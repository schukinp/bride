import pytest
from pages.home_page import HomePage
from pages.dashboard_page import DashboardPage
from data import *


@pytest.mark.usefixtures('open_base_url')
class TestLogin():
    def test_unsuccessfull_login(self):
        """check user cannot login with wrong password"""
        HomePage().login_as(registered_user, invalid_password)
        HomePage().check_login_error_is('Wrong password!')
        HomePage().close_popup()

    def test_successfull_login(self):
        """check user can successfully login"""
        HomePage().login_as(registered_user, registered_password)
        DashboardPage().check_user_is_logged_in()

