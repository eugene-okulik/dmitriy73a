class LocatorsCart:
    HEADER_TITLE = ".mb-4"
    ALERT_MESSAGE = ".js_cart_lines"
    PRODUCTS_TITLE = '.o_wsale_products_item_title'
    BUTTON_ADD = "#add_to_cart"
    BUTTON_CONTINUE = ".btn.btn-secondary"
    QUANTITY_IN_CART = '.my_cart_quantity'
    BUTTON_CART = ".fa.fa-shopping-cart.fa-stack"
    TITLE_PRODUCT_IN_CART = ".d-inline"
    BLOCK_SUMM = ".card-body"
    SUBTOTAL = "#cart_total_subtotal"
    DISCOUNT_FIELD = '//input[@class="form-control"]'
    BUTTON_APPLY = '//a[text()="Apply"]'
    ALERT_NO_DISCOUNT = '//div[@role="alert"]'


class LocatorsCategory:
    FIELDS_SEARCH = '//input[@type="search"]'
    BUTTON_GLASS = ".btn.oe_search_button.btn.btn-light"
    PRODUCTS_TITLE = '.o_wsale_products_item_title'
    MESS_NO_RESULT = ".mt8"
    MESS_NO_RESULT_UNDER = '//*[contains(text(), "No results for")]'
    PRICE_RANGE = '.multirange-wrapper'
    CHECKBOX_ALUM = "[id='1-2']"
    PRODUCT_IMAGES = '.oe_product_image'
    SWITCHER_PRICELIST = "//a[@data-bs-toggle='dropdown' and @role='button']"
    SWITCHER_EUR = '//span[text()="EUR"]'
    PRODUCT_PRICE = ".product_price"


class LocatorsProduct:
    TITLE_PRODUCT = "//h1"
    CURRENCY_VALUE = ".oe_currency_value"
    BUTTON_REMOVE = '//a[@title="Remove one"]'
    BUTTON_ADD = '//a[@title="Add one"]'
    FIELD_COUNT = '//input[@name="add_qty"]'
    BUTTON_ADD_CART = '#add_to_cart'
    QUANTITY_IN_CART = '.my_cart_quantity'
    BUTTON_CART = ".fa.fa-shopping-cart.fa-stack"
    TITLE_PRODUCT_IN_CART = ".d-inline"
    FIELDS_SEARCH = '//input[@type="search"]'
    BUTTON_GLASS = ".btn.oe_search_button.btn.btn-light"
    MESS_NO_RESULT = ".mt8"
    MESS_NO_RESULT_UNDER = '//*[contains(text(), "No results for")]'
