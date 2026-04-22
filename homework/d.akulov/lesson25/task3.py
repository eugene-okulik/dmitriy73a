from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_task3_1(driver_chrome):
    driver_chrome.get("https://www.qa-practice.com/elements/select/single_select")
    dropdown = driver_chrome.find_element(By.ID, "id_choose_language")
    select = Select(dropdown)
    select.select_by_visible_text("C#")
    dropdown.click()
    driver_chrome.find_element(By.ID, "submit-id-submit").click()
    assert driver_chrome.find_element(By.ID, "result-text").text == "C#"


def test_task3_2(driver_chrome):
    wait = WebDriverWait(driver_chrome, 6)
    driver_chrome.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    start = driver_chrome.find_element(By.TAG_NAME, "button")
    start.click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="finish"]/h4'), "Hello World!"))
    assert driver_chrome.find_element(By.XPATH, '//*[@id="finish"]/h4').text == "Hello World!"
