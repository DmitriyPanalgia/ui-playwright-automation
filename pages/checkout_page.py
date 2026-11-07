from playwright.sync_api import Page


class CheckoutPage:


    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.postal_code = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.error_message = page.locator("[data-test='error']")
        self.finish_button = page.get_by_role("button", name="Finish")
        self.complete_header = page.locator(".complete-header")
        self.products_names = page.locator(".inventory_item_name")
        self.products_prices = page.locator(".inventory_item_price")
        self.subtotal_price = page.locator(".summary_subtotal_label")
        self.tax_price = page.locator(".summary_tax_label")
        self.total_price = page.locator(".summary_total_label")


    def enter_first_name(self, first_name: str):
        self.first_name.fill(first_name)


    def enter_last_name(self, last_name: str):
        self.last_name.fill(last_name)


    def enter_postal_code(self, postal_code: str):
        self.postal_code.fill(postal_code)


    def click_continue(self):
        self.continue_button.click()


    def get_error_message(self):
        return self.error_message


    def click_finish_order(self):
        self.finish_button.click()
