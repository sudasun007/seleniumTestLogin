
# README for Selenium Test Automation

## Overview
This project contains test automation scripts for testing the login functionality, navigation, and dashboard display of a sample website that I created specifically for this purpose. The website URL is embedded in the code: `https://testwebsitesudh.netlify.app/`.

The tests are implemented using Python's `unittest` framework and Selenium WebDriver.

---

## Prerequisites
Ensure the following software and tools are installed:

1. **Python** (Version 3.7 or higher)
   - Download and install Python from [python.org](https://www.python.org/).
   - Ensure Python is added to your system's PATH.

2. **Google Chrome Browser**
   - Download and install the latest version of Google Chrome from [google.com/chrome](https://www.google.com/chrome/).

3. **ChromeDriver**
   - Download the version of ChromeDriver matching your Chrome browser version from [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads).
   - Add the ChromeDriver executable to your system's PATH.

4. **Python Libraries**
   - Install the required Python packages using pip:

```bash
pip install selenium
```

5. **IDE (Optional)**
   - Use an Integrated Development Environment like PyCharm, VSCode, or any text editor of your choice for editing and running the scripts.

---

## Project Setup

1. Clone or download this repository to your local machine.
2. Navigate to the project directory:

```bash
cd <project_directory>
```

3. Create a directory for storing screenshots of test results:

```bash
mkdir test_results_Testsite
```

4. Verify that the ChromeDriver executable is in your system's PATH and matches the installed version of Google Chrome.

---

## How to Execute the Tests

1. Open a terminal or command prompt and navigate to the project directory.
2. Run the test suite using the following command:

```bash
python <script_name>.py
```

Replace `<script_name>` with the name of the file containing the test script (e.g., `test_script.py`).

3. During execution, screenshots for different test steps will be saved in the `test_results_Testsite` directory.

4. Test results will be displayed in the terminal output.

---

## Test Cases

1. **Login Functionality**
   - Tests login with valid and invalid credentials.
   - Screenshots: `invalid_login.png`, `valid_login.png`.

2. **Navigation After Login**
   - Tests navigation through different sections of the website.
   - Screenshots: `navigation_test_link_1.png`, `navigation_test_link_2.png`, etc.

3. **Dashboard Display**
   - Verifies the presence of the dashboard and welcome message after a successful login.
   - Screenshot: `dashboard_display.png`.

---

## Notes

- The project is designed for educational purposes and uses a custom test website.
- Adjust timeouts in the script as needed, depending on your system's performance.
- Update the website URL in the script if it changes.

---

## Troubleshooting

1. **Error: "ChromeDriver executable needs to be in PATH"**
   - Ensure ChromeDriver is installed and added to the PATH.

2. **Error: "TimeoutException"**
   - Increase the WebDriver wait time in the script.

3. **Error: "ModuleNotFoundError" for Selenium**
   - Ensure Selenium is installed using pip.

4. **Browser Compatibility Issues**
   - Ensure the ChromeDriver version matches your installed Chrome browser version.

---

## Author
This project and the accompanying test website were created for demonstration purposes by Sudheera. Feel free to reach out for questions or contributions.

---
