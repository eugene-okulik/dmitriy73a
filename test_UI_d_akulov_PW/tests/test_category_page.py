def test_search_product_in_category(category):
    category.open_page()
    category.search_in_category_positive("Four Person Desk")
    category.search_in_category_negative("Warranty")


def test_filter_legs(category):
    category.open_page()
    category.filter_by_legs()
    category.check_after_filter()


def test_change_currency(category):
    category.open_page()
    category.check_field_switch_currency()
    category.check_currency_product("$")
    category.switch_currency_eur()
    category.check_currency_product("€")
    category.check_field_switch_currency()
