from playwright.sync_api import expect
import pytest


@pytest.mark.parametrize(
    "product_names",
    [
        ("Sauce Labs Backpack",),
        ("Sauce Labs Backpack", "Sauce Labs Bike Light"),
        ("Sauce Labs Backpack","Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt",)
    ]
)
def test_add_products_to_cart(authenticated_inventory_page,
                             cart_page_object,
                              product_names):
    for product_name in product_names:
        authenticated_inventory_page.add_product_to_cart(product_name)


    expect(authenticated_inventory_page.cart_link).to_have_text(str(len(product_names)))
    cart_page_object.open()

    for product_name in product_names:
        expect(cart_page_object.get_item(product_name)).to_be_visible()


    expect(cart_page_object.cart_items).to_have_count(len(product_names))


def test_remove_product_from_cart(authenticated_inventory_page,
                                  cart_page_object,):

    authenticated_inventory_page.add_product_to_cart("Sauce Labs Backpack")
    authenticated_inventory_page.add_product_to_cart("Sauce Labs Bike Light")
    cart_page_object.open()
    cart_page_object.remove_item("Sauce Labs Bike Light")

    expect(cart_page_object.cart_link).to_have_text("1")
    expect(cart_page_object.get_item("Sauce Labs Bike Light")).to_have_count(0)
    expect(cart_page_object.get_item("Sauce Labs Backpack")).to_be_visible()
    expect(cart_page_object.cart_items).to_have_count(1)


def test_remove_last_product_from_cart(authenticated_inventory_page,
                                       cart_page_object,):

    authenticated_inventory_page.add_product_to_cart("Sauce Labs Backpack")
    cart_page_object.open()
    cart_page_object.remove_item("Sauce Labs Backpack")

    expect(cart_page_object.cart_items).to_have_count(0)
    expect(cart_page_object.cart_badge).to_be_hidden()