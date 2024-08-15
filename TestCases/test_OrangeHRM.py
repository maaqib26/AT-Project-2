"""
test_OrangeHRM.py - Script to validate Login and PIM test cases
"""

# Import necessary libraries
from Locators.OrangeHRM_Locators import Locators
from Utilities.excel_functions import Excel_Operations
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.action_chains import ActionChains


# Load test data from Excel file
test_data_excel_file = Locators().excel_file
test_sheet_number = Locators().sheet_number

# Create an object for the excel class
excel_handler = Excel_Operations(test_data_excel_file,test_sheet_number)

# Read test data from Excel file
test_username = excel_handler.read_data(2,7)
test_password = excel_handler.read_data(2,8)

# Define a test class for OrangeHRM login
class Test_OrangeHRM_Login():
    # Fixture to set up and tear down the browser
    @pytest.fixture
    def boot(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver,60)
        self.driver.get(Locators.url)
        yield
        # Close the browser after the test is complete
        self.driver.close()

    # Method for Login
    def login(self):
        """
        Method for logging into OrangeHRM Portal
        """
        try:
            # Enter the username and password
            valid_username = self.wait.until(EC.presence_of_element_located((By.NAME,Locators().username)))
            valid_username.send_keys(test_username)
            valid_password = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().password)))
            valid_password.send_keys(test_password)

            # Click the login button
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators().submit_button)))
            login_button.click()

        # Check if the login was successful
            if Locators().dashboard_url == self.driver.current_url:
                # print("SUCCESS : Login with Valid Username {a} & Password {b}".format(a=test_username, b=test_password))
                # excel_handler.write_data(2,12,Locators.pass_data)
                # Assert that Login is successful
                assert True, "Login successful"
            else:
                # print("ERROR : Unable to Login with Username {a} & Password {b}".format(a=test_username, b=test_password))
                # excel_handler.write_data(2, 12, Locators.fail_data)
                # Assert that Login is unsuccessful
                assert False, "Login Unsuccessful with valid username & password"

        # Handle any exceptions that may occur
        except (NoSuchElementException, ElementNotVisibleException) as e:
            print("ERROR : ", e)


    def test_TC_PIM_01(self, boot):
        """
        TC ID - TC_PIM_01
        Test Objective - Forgot Password link validation on login page
        """
        try:
            # Click on the Forgot Password Link
            forgot_password = self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators().forgot_password)))
            forgot_password.click()
            
            # Verify is the username is visible and then enter the username from the excel
            username = self.wait.until(EC.presence_of_element_located((By.NAME,Locators().forgot_password_username)))
            if username.is_displayed():
                username.send_keys(test_username)
            else:
                print("Username is not visible")

            # Click on the reset button
            reset_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators().reset_password_button)))
            reset_button.click()

            # Wait for the reset confirmation message to appear
            reset_confirmation = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().reset_password_success)))

            # Check if the password reset was successful
            if reset_confirmation.text == Locators().reset_confim_print:
                print("SUCCSS: Password Reset is successful")
                excel_handler.write_data(2, 9, Locators().pass_data)
            else:
                print("ERROR: Password Reset not successful")
                excel_handler.write_data(2, 9, Locators().fail_data)
            assert reset_confirmation.text == Locators().reset_confim_print , "Assertion failed: Reset not successful."

            # Handle any exceptions that may occur
        except (NoSuchElementException, ElementNotVisibleException) as e:
            print("ERROR : ", e)


    def test_TC_PIM_02(self,boot):
        """
        TC ID - TC_PIM_02
        Test Objective - Header Validation on Admin Page
        """

        # Login using the login method defined
        self.login()
        try:

            # Initialize the ActionChains object
            actions = ActionChains(self.driver)

            # Click on the Admin menu item
            admin = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, Locators().admin)))
            actions.move_to_element(admin).perform()
            admin.click()

            # Initialize index to 1
            index = 1

            # Wait for all elements to be present on the page that match the XPath locator for admin headers
            admin_elements = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, Locators().admin_header)))

            # Iterate over each element found
            for elements in admin_elements:
                # Check if the element is displayed on the page
                if elements.is_displayed():
                    # Print a success message with the text of the element
                    print(f"{index}. SUCCESS: Admin Page Header '{elements.text}' is visible")
                    # Write pass data to an Excel file
                    excel_handler.write_data(3, 9, Locators().pass_data)
                    # Increment the index
                    index += 1
                else:
                    # Print an error message if the element is not visible
                    print("ERROR: Admin Header Element/Elements are not visible")
                    # Write fail data to an Excel file
                    excel_handler.write_data(3, 9, Locators().fail_data)
                # Assert that the element is displayed, and raise an AssertionError if it's not
                assert elements.is_displayed(), f"Assertion failed: {elements} is not visible"

        # Handle any exceptions that may occur
        except (NoSuchElementException, ElementNotVisibleException) as e:
            print("ERROR : ", e)

    def test_TC_PIM_03(self, boot):
        """
        TC ID - TC_PIM_03
        Test Objective - Main Menu Validation on Admin Page
        """
        # Login using the login method defined
        self.login()
        try:
            # Initialize the ActionChains object
            actions = ActionChains(self.driver)

            # Click on the Admin menu item
            admin = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, Locators().admin)))
            actions.move_to_element(admin).perform()
            admin.click()

            # Initialize index to 1
            index = 1

            # Wait for all elements to be present on the page that match the XPath locator for side menu
            side_menu_elements = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, Locators().side_pane)))

            # Iterate over each element found
            for elements in side_menu_elements:
                # Check if the element is displayed on the page
                if elements.is_displayed():
                    # Print a success message with the text of the element
                    print(f"{index}. SUCCESS: Side Pane Menu Option '{elements.text}' is visible")
                    # Write pass data to an Excel file
                    excel_handler.write_data(4, 9, Locators().pass_data)
                    # Increment the index
                    index += 1
                else:
                    # Print an error message if the element is not visible
                    print("ERROR: Side Pane Menu Element/Elements are not visible")
                    # Write fail data to an Excel file
                    excel_handler.write_data(4, 9, Locators().fail_data)
                # Assert that the element is displayed, and raise an AssertionError if it's not
                assert elements.is_displayed(), f"Assertion failed: {elements} is not visible"

        # Handle any exceptions that may occur
        except (NoSuchElementException, ElementNotVisibleException) as e:
            print("ERROR : ", e)

    