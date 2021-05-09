import random
import pytest
from pages.my_account_page import MyAccountPage


#driver = webdriver.Chrome(ChromeDriverManager().install())
@pytest.mark.usefixtures("setup")


class TestCreateAccount:

    def test_create_account_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account("lucas@gmail.com", "tester123456789$")

        msg = 'An account is already registered with your email address. Please log in.'
        assert msg in my_account_page.get_error_msg()

    def test_create_account_passed(self):

        email = str(random.randint(0,10000)) + "lucas@gmail.com"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "tester123456789$")

        assert my_account_page.is_logout_link_displayed()