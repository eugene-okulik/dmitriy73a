from playwright.sync_api import Page


def test_task3(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")
    button_text = page.locator('.text-danger')
    button_text.click()
