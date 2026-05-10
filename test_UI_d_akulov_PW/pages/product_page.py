from pages.base_page import BasePage
from pages.locators.locators_cart import LocatorsProduct
from playwright.sync_api import expect


class ProductPage(BasePage):
    page_url = "shop/furn-9999-office-design-software-7?category=9"

    def check_title_product(self, title):
        title_product = self.find(LocatorsProduct.TITLE_PRODUCT)
        expect(title_product).to_have_text(title)

    def check_currency_value(self):
        currency_value = self.find(LocatorsProduct.CURRENCY_VALUE).first
        expect(currency_value).to_be_visible()
        assert float(currency_value.inner_text()) > 0

    def check_field_count_and_add(self):
        expect(self.find(LocatorsProduct.BUTTON_REMOVE)).to_be_visible()
        expect(self.find(LocatorsProduct.BUTTON_ADD)).to_be_visible()
        expect(self.find(LocatorsProduct.FIELD_COUNT)).to_be_visible()
        expect(self.find(LocatorsProduct.BUTTON_ADD)).to_be_visible()

    def add_to_cart(self):
        self.find(LocatorsProduct.BUTTON_ADD_CART).click()
        expect(self.page.locator(".toast-body")).to_be_visible()
        title_product = self.find(LocatorsProduct.TITLE_PRODUCT).inner_text()
        self.find(LocatorsProduct.BUTTON_CART).first.click()
        return title_product

    def field_search(self, product):
        search_field = self.page.get_by_role("searchbox", name="Search...")
        search_field.fill(product)
        self.find(LocatorsProduct.BUTTON_GLASS).click()

    def check_no_results_after_search(self, product):
        text_no_results = self.find(LocatorsProduct.MESS_NO_RESULT)
        text_under_no_results = self.find(LocatorsProduct.MESS_NO_RESULT_UNDER)
        expect(text_no_results).to_have_text("No results")
        expect(text_under_no_results).to_have_text(f'No results for "{product}" in category "Multimedia".')
