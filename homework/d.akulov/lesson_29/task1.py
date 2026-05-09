from playwright.sync_api import Page, expect


def test_task1(page: Page):
    page.on('dialog', lambda alert: alert.accept())
    page.goto("https://www.qa-practice.com/elements/alert/confirm#")
    page.locator(".a-button").click()
    selected_block = page.locator("#result")
    expect(selected_block).to_be_visible()
    result_text = page.locator("#result-text")
    expect(result_text).to_have_text("Ok")
