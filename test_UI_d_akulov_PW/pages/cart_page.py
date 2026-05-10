from pages.base_page import BasePage
from pages.locators.locators_cart import LocatorsCart
from playwright.sync_api import expect


class CartPage(BasePage):
    page_url = "shop/cart"

    def check_header_title(self, title):
        header_title = self.find(LocatorsCart.HEADER_TITLE)
        expect(header_title, "заголовок корзины изменился").to_have_text(title)

    def check_alert_message_empty_cart(self, alert):
        alert_message = self.find(LocatorsCart.ALERT_MESSAGE)
        expect(alert_message, "заголовок корзины изменился").to_have_text(alert)

    def check_product_in_cart(self, product):
        title_product_in_cart = self.find(LocatorsCart.TITLE_PRODUCT_IN_CART)
        expect(title_product_in_cart, "товар в корзине не найден либо не тот").to_have_text(product)

    def check_block_total_summ_product_in_cart(self):
        expect(self.find(LocatorsCart.BLOCK_SUMM), "блок суммы товаров не отображается").to_be_visible()

    def check_block_total_summ_fields(self):
        expect(self.find(LocatorsCart.SUBTOTAL)).to_have_text("Subtotal")
        expect(self.find(LocatorsCart.DISCOUNT_FIELD), "нет поля ввода discount code").to_be_visible()

    def check_alert_input_invalid_discount_code(self, code):
        self.find(LocatorsCart.DISCOUNT_FIELD).fill(code)
        self.find(LocatorsCart.BUTTON_APPLY).click()
        expect(self.find(LocatorsCart.ALERT_NO_DISCOUNT)).to_have_text("This promo code is not available.")
