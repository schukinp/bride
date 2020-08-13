from selene.api import *

#locators
profile_avatar_icon = s('.profile-info-avatar')


#class for home page methods
class DashboardPage():
    def check_user_is_logged_in(self):
        profile_avatar_icon.should(be.in_dom)
