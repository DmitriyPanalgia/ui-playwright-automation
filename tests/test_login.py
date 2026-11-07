from playwright.sync_api import expect
from config import BASE_URL



def test_successful_login(login_page,
                          inventory_page_object
                          ):


    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    expect(login_page.page).to_have_url(f"{BASE_URL}/inventory.html")
    expect(inventory_page_object.page_title).to_be_visible()


def test_login_with_wrong_password(login_page):


    login_page.enter_username("standard_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()

    expect(login_page.page).to_have_url(f"{BASE_URL}/")
    expect(login_page.get_error_message()).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )



def test_login_with_empty_login(login_page):


    login_page.enter_username("")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    expect(login_page.page).to_have_url(f"{BASE_URL}/")
    expect(login_page.get_error_message()).to_have_text(
            "Epic sadface: Username is required"
    )



def test_login_locked_out_user(login_page):

    login_page.enter_username("locked_out_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    expect(login_page.page).to_have_url(f"{BASE_URL}/")
    expect(login_page.get_error_message()).to_have_text(

            "Epic sadface: Sorry, this user has been locked out."
    )
