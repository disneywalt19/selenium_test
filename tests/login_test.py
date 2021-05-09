from pages.my_account_page import MyAccountPage
import pytest


#driver = webdriver.Chrome(ChromeDriverManager().install())

@pytest.mark.usefixtures("setup")
class TestLogIn:

    def test_log_in_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("lucas@gmail.com", "tester123456789$")

        assert my_account_page.is_logout_link_displayed()

    def test_log_in_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("lucaswthth@gmail.com", "tester123456789$rtgrth")

        assert "ERROR: Incorrect username or password." in my_account_page.get_error_msg()
