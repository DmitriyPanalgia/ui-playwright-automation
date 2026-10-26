from playwright.sync_api import Page


class CartPage:


    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.cart_link = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.checkout_button = page.get_by_role("button", name="Checkout")


    def open(self):
        self.cart_link.click()


    def get_item(self, product_name: str):
        return self.cart_items.filter(has_text=product_name)


    def remove_item(self, product_name: str):
        self.get_item(product_name).get_by_role("button", name="Remove").click()


    def checkout(self):
        self.checkout_button.click()

