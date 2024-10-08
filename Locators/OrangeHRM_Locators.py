"""
OrangeHRM_Locators.py - Script to store web element locators
"""

class Locators:
    username = "username"
    password = "password"
    submit_button = "//button[@type='submit']"
    forgot_password = "//div[@class='orangehrm-login-forgot']//p"
    forgot_password_username = "username"
    reset_password_button = "//div[@class='orangehrm-forgot-password-button-container']//button[2]"
    reset_password_success = "//div[@class='orangehrm-card-container']//h6"
    reset_confim_print = "Reset Password link sent successfully"
    admin = "Admin"
    admin_header = "//div//nav[@aria-label='Topbar Menu']//ul//li"
    side_pane = "//div//nav[@aria-label='Sidepanel']//ul//li"
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    excel_file = "E:\\Workspace\\GUVI\\PAT-Projects\\AT-Project-2\\Data\\test_data.xlsx"
    sheet_number = "Test_Data"
    pass_data = "TEST PASS"
    fail_data = "TEST FAILED"
