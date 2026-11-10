from playwright.sync_api import Page , expect



def test_login_page_title(open_app: Page):


    expect(open_app).to_have_title("Swag Labs")


def test_login_form_visible(open_app: Page):


    username = open_app.get_by_placeholder("Username")
    password = open_app.get_by_placeholder("Password")
    login_button = open_app.get_by_role("button", name="Login")

    expect(username).to_be_visible()
    expect(password).to_be_visible()
    expect(password).to_have_attribute("type", "password")
    expect(login_button).to_be_visible()


