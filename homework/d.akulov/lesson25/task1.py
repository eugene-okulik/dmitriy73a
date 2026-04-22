from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_task1(driver_chrome):
    driver_chrome.get("https://www.qa-practice.com/elements/input/simple")
    input = driver_chrome.find_element(By.XPATH, '//*[@id="id_text_string"]')
    input.send_keys("q")
    input.send_keys(Keys.ENTER)
    element = driver_chrome.find_element(By.ID, "error_1_id_text_string")
    assert element.get_attribute("innerText") == "Please enter 2 or more characters"
    assert element.value_of_css_property("color") == "rgba(255, 0, 0, 1)"



def test_task1_2(driver_chrome):
    driver_chrome.get("https://www.qa-practice.com/elements/input/simple")
    input = driver_chrome.find_element(By.CSS_SELECTOR, '[id="id_text_string"]')
    input.send_keys("qwerty")
    input.submit()
    element = driver_chrome.find_element(By.CLASS_NAME, "result-text")
    assert element.text == "qwerty"
    print(element.text)

