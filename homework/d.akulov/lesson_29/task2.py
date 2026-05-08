from playwright.sync_api import Page, expect, BrowserContext


def test_task2(page: Page, context: BrowserContext):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    link = page.locator('#new-page-button')
    with context.expect_page() as new_page_event:
        link.click()

    new_page = new_page_event.value
    text_on_new_page = new_page.locator("#result-text")
    expect(text_on_new_page).to_have_text("I am a new page in a new tab")

    page.bring_to_front()
    expect(link).to_be_enabled()
    new_page.close()
