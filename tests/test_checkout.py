from playwright.sync_api import expect
import pytest
import allure


@allure.feature("Оформление заказа")
@allure.story("Отображение формы")
@allure.title("Отображение полей оформления заказа")
def test_checkout_form_visible(authenticated_inventory_page,
                               cart_page_object,
                               checkout_page_object):

    authenticated_inventory_page.add_product_to_cart("Sauce Labs Backpack")
    cart_page_object.open()
    cart_page_object.checkout()


    expect(checkout_page_object.first_name).to_be_visible()
    expect(checkout_page_object.last_name).to_be_visible()
    expect(checkout_page_object.postal_code).to_be_visible()


@allure.feature("Оформление заказа")
@allure.story("Валидация обязательных полей")
@allure.title("Проверка обязательных полей оформления заказа")
@pytest.mark.parametrize(
    "first_name, last_name, postal_code, expected_error_message",
    [
        ("","Ivanov","12345","Error: First Name is required"),
        ("Dima", "", "12345", "Error: Last Name is required"),
        ("Dima", "Ivanov", "", "Error: Postal Code is required")
    ],
    ids= [
        "Пустое имя",
        "Пустая фамилия",
        "Пустой почтовый индекс"
    ]
)
def test_checkout_required_fields_validation(authenticated_inventory_page,
                                     cart_page_object,
                                     checkout_page_object,
                                     first_name,
                                     last_name,
                                     postal_code,
                                     expected_error_message):

    authenticated_inventory_page.add_product_to_cart("Sauce Labs Backpack")
    cart_page_object.open()
    cart_page_object.checkout()

    checkout_page_object.enter_first_name(first_name)
    checkout_page_object.enter_last_name(last_name)
    checkout_page_object.enter_postal_code(postal_code)
    checkout_page_object.click_continue()

    expect(checkout_page_object.get_error_message()).to_have_text(expected_error_message)


@allure.feature("Оформление заказа")
@allure.story("Успешное оформление заказа")
@allure.title("Успешное оформление заказа с проверкой стоимости")
def test_successful_checkout(authenticated_inventory_page,
                             cart_page_object,
                             checkout_page_object):

    authenticated_inventory_page.add_product_to_cart("Sauce Labs Backpack")
    authenticated_inventory_page.add_product_to_cart("Sauce Labs Bike Light")
    cart_page_object.open()
    cart_page_object.checkout()

    checkout_page_object.enter_first_name("Dima")
    checkout_page_object.enter_last_name("Ivanov")
    checkout_page_object.enter_postal_code("12345")
    checkout_page_object.click_continue()

    expect(checkout_page_object.products_names).to_have_text(
        ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    )
    expect(checkout_page_object.products_prices).to_have_text(["$29.99", "$9.99"])
    expect(checkout_page_object.subtotal_price).to_have_text("Item total: $39.98")
    expect(checkout_page_object.tax_price).to_have_text("Tax: $3.20")
    expect(checkout_page_object.total_price).to_have_text("Total: $43.18")

    checkout_page_object.click_finish_order()

    expect(checkout_page_object.complete_header).to_have_text(
        "Thank you for your order!"
    )

