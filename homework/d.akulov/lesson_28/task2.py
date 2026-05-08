from playwright.sync_api import Page


def test_task2(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")

    page.get_by_placeholder("First Name").fill("Tot")
    page.get_by_placeholder("Last Name").fill("Samiy")
    page.get_by_placeholder("name@example.com").fill("togo@samogo.com")
    page.get_by_text("Other").click()
    page.get_by_placeholder("Mobile Number").fill("0123456789")

    page.locator("#dateOfBirthInput").click()
    page.locator(".react-datepicker__month-select").select_option("11")
    page.locator(".react-datepicker__year-select").select_option("1900")
    page.get_by_label("Choose Tuesday, December 18th, 1900").click()

    subInp = page.locator("#subjectsInput")
    subInp.press_sequentially("Math", delay=10)
    subInp.press("Enter")
    subInp.press_sequentially("Arts", delay=10)
    subInp.press("Enter")

    page.get_by_text("Sports").click()
    page.get_by_text("Reading").click()
    page.get_by_text("Music").click()

    page.get_by_placeholder("Current Address").fill("qwerty")

    state = page.locator("#react-select-3-input")
    state.press_sequentially("NCR")
    state.press("Enter")

    city = page.locator("#react-select-4-input")
    city.press_sequentially("Delhi")
    city.press("Enter")

    page.get_by_text("Submit").click()
