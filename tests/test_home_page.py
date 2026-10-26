from playwright.sync_api import Page , expect



def test_login_page_title(login_page: Page):


    expect(login_page).to_have_title("Swag Labs")


def test_login_form_visible(login_page: Page):


    username = login_page.get_by_placeholder("Username")
    password = login_page.get_by_placeholder("Password")
    login_button = login_page.get_by_role("button", name="Login")

    expect(username).to_be_visible()
    expect(password).to_be_visible()
    expect(password).to_have_attribute("type", "password")
    expect(login_button).to_be_visible()


