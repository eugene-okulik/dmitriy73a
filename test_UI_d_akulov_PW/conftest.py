import pytest
from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from playwright.sync_api import BrowserContext


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def cart(page):
    return CartPage(page)


@pytest.fixture()
def category(page):
    return CategoryPage(page)


@pytest.fixture()
def product(page):
    return ProductPage(page)
