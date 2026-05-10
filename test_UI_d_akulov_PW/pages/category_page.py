import re
from pages.base_page import BasePage
from pages.locators.locators_cart import LocatorsCategory
from playwright.sync_api import expect


class CategoryPage(BasePage):
    page_url = "shop/category/desks-1"

    def search_in_category_positive(self, product):
        search_field = self.page.get_by_role("searchbox", name="Search...")
        search_field.fill(product)
        self.page.get_by_role("button", name="Search").click()
        expect(self.page).to_have_url(re.compile("category=1&search=Four"))
        expect(self.find(LocatorsCategory.PRODUCTS_TITLE)).to_have_text(product)

    def search_in_category_negative(self, product):
        search_field = self.page.get_by_role("searchbox", name="Search...")
        search_field.clear()
        search_field.fill(product)

        self.page.get_by_role("button", name="Search").click()

        expect(self.page).to_have_url(re.compile("search=Warranty"))

        text_no_results = self.find(LocatorsCategory.MESS_NO_RESULT)
        text_under_no_results = self.find(LocatorsCategory.MESS_NO_RESULT_UNDER)

        expect(text_no_results).to_have_text("No results")
        expect(text_under_no_results).to_have_text(f'No results for "{product}" in category "Desks".')

    def filter_by_legs(self):
        expect(self.find(".multirange-wrapper").first).to_be_visible()
        self.find(LocatorsCategory.CHECKBOX_ALUM).first.click()
        expect(self.page).to_have_url(re.compile("attrib=1-2"))

    def check_after_filter(self):
        count_product = self.find(LocatorsCategory.PRODUCT_IMAGES).count()
        text_product = self.find(LocatorsCategory.PRODUCTS_TITLE)

        assert count_product == 1
        expect(text_product).to_have_text("Customizable Desk")

    def switch_currency_eur(self):
        switcher_pricelist = self.find(LocatorsCategory.SWITCHER_PRICELIST).first
        switcher_pricelist.click()

        eur = self.find(LocatorsCategory.SWITCHER_EUR)
        eur.click()

    def check_currency_product(self, currency):
        expect(self.find(LocatorsCategory.PRODUCT_PRICE).first).to_contain_text(currency)

    def check_field_switch_currency(self):
        switcher_pricelist = self.find(LocatorsCategory.SWITCHER_PRICELIST).first
        expect(switcher_pricelist, "поле выбора валюты не отображается").to_be_visible()
