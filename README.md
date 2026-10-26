# UI Playwright Automation

## About the Project

This project contains automated UI tests for the [SauceDemo](https://www.saucedemo.com/) web application using Python, Playwright, and pytest.

The project follows the Page Object Model (POM) design pattern to separate page interaction logic from test scenarios.

## Technologies

- Python
- Playwright
- pytest
- pytest-playwright
- Page Object Model (POM)

## Test Coverage

### Login
- Successful login
- Login with an incorrect password
- Login with an empty username
- Login with a locked-out user

### Home Page
- Verify page title
- Verify login form elements are visible
- Verify password field is masked

### Shopping Cart
- Add one or multiple products to the cart
- Verify cart contents and product count
- Remove a product from the cart
- Remove the last product and verify the cart badge is hidden

### Checkout
- Verify checkout form fields
- Validate required checkout fields
- Verify product details and order price calculation
- Complete an order successfully

## Project Structure

```text
ui_playwright_automation/
├── pages/
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── inventory_page.py
│   └── login_page.py
├── tests/
│   ├── conftest.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_home_page.py
│   └── test_login.py
├── config.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd ui_playwright_automation
```

Replace `<repository-url>` with the URL of your GitHub repository.

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Install the Playwright browser

```bash
python -m playwright install chromium
```

## Running Tests

Run the complete test suite:

```bash
python -m pytest -v
```

## Test Application

Tests run against the public SauceDemo demo application.

The test suite uses the application's demo accounts and is intended for learning and portfolio demonstration purposes.
