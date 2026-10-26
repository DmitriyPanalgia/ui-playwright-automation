import pytest
from playwright.sync_api import Page, expect
from config import BASE_URL
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def login_page(page: Page):
    page.goto(BASE_URL)
    return page


@pytest.fixture
def login_page_object(login_page: Page):
    return LoginPage(login_page)


@pytest.fixture
def inventory_page_object(login_page: Page):
    return InventoryPage(login_page)


@pytest.fixture
def authenticated_inventory_page(login_page_object,
                                 inventory_page_object):
    login_page_object.enter_username("standard_user")
    login_page_object.enter_password("secret_sauce")
    login_page_object.click_login()

    expect(login_page_object.page).to_have_url(f"{BASE_URL}/inventory.html")
    expect(inventory_page_object.page_title).to_be_visible()

    return inventory_page_object


@pytest.fixture
def cart_page_object(authenticated_inventory_page):
    return CartPage(authenticated_inventory_page.page)


@pytest.fixture
def checkout_page_object(cart_page_object):
    return CheckoutPage(cart_page_object.page)