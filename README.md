
# Overview

This script contains test cases for validating various functionalities on the OrangeHRM portal. It uses Selenium WebDriver for browser automation and Pytest for managing and running the tests. The tests are designed to check login functionality, password reset, header validation, and menu validation.

# Test Objectives

1. #### Login Functionality: 
Ensure that users can log in with valid credentials and handle incorrect login attempts.

2. ### Password Reset: 
Validate the password reset functionality, including verification of the success message.

3. #### Header Validation: 
Verify that all expected headers are visible on the Admin page.

4. #### Menu Validation: 
Check that all expected menu items are present and visible on the Admin page.

# Prerequisites

* Python 3.x

* pip package manager

* Chrome browser installed

* The following Python packages installed via pip:

    * selenium
    * pytest
    * openpyxl
    * webdriver-manager

You can install the required packages using the following command:

```bash
  pip install selenium pytest openpyxl webdriver-manager
```

# How to Run the Tests

1. Clone the Repository: Clone this repository to your local machine.

2. Set Up Excel Data: Ensure that the test_data.xlsx file is correctly formatted and contains the necessary data for the test cases.

3. Run the Tests: Use pytest to run the test cases in the test_OrangeHRM.py script.

```bash
  pytest test_OrangeHRM.py
```
# Test Cases

1. #### test_TC_PIM_01:

* Objective: Validate the "Forgot Password" link functionality.
*  Steps:
      
        1. Click the "Forgot Password" link.
        2. Enter the username and click the reset button.
        3. Verify the reset confirmation message.

2. #### test_TC_PIM_02:

* Objective: Validate headers on the Admin page.
* Steps:

        1. Log in to the portal.
        2. Navigate to the Admin page.
        3. Verify the presence and visibility of expected headers.


3. #### test_TC_PIM_03:

* Objective: Validate menu items on the Admin page.
* Steps:

      1. Log in to the portal.
      2. Navigate to the Admin page.
      3. Verify the presence and visibility of expected menu items.

# Error Handling

The script includes exception handling to manage common Selenium exceptions like NoSuchElementException and ElementNotVisibleException, ensuring that the test cases provide meaningful error messages in case of failure.

# Logging and Reporting

The script prints success or error messages to the console for each test case, including the specific actions performed (e.g., login success/failure, employee details update/delete status). The test results are also logged in the Excel file for reference.

# Notes

Ensure that the correct ChromeDriver version is being used for your version of the Chrome browser.
Update the Locators.py file with the correct locators and URLs relevant to your OrangeHRM instance.



