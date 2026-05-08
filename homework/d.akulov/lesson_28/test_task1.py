from playwright.sync_api import Page


def test_task1(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    link = page.get_by_role("link", name="Form Authentication")
    link.click()
    page.get_by_role("textbox", name="username").fill("tomsmith")
    page.get_by_role("textbox", name="password").fill("SuperSecretPassword!")
    page.get_by_role("button").click()
