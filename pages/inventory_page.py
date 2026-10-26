from playwright.sync_api import Page


class InventoryPage:


    def __init__(self, page: Page):

        self.page = page
        self.page_title = page.get_by_text("Products", exact=True)
        self.cart_link = page.locator(".shopping_cart_link")


    def add_product_to_cart(self, product_name: str):
        product = self.page.locator(".inventory_item").filter(
            has_text=product_name
        )
        product.get_by_role("button", name="Add to cart").click()


    def open_cart(self):
        self.cart_link.click()