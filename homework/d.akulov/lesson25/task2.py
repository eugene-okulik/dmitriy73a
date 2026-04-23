from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def test_task2(driver_chrome):
    # не понял про рекламу, все равно решил помучаться с мобилкой
    driver_chrome.set_window_size(414, 896)
    wait = WebDriverWait(driver_chrome, 5)

    driver_chrome.get("https://demoqa.com/automation-practice-form")

    first_name = driver_chrome.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]')
    first_name.send_keys("Tot")

    last_name = driver_chrome.find_element(By.ID, 'lastName')
    last_name.send_keys("Samiy")

    email = driver_chrome.find_element(By.XPATH, '//*[@id="userEmail"]')
    email.send_keys("tot@test.com")

    gender = driver_chrome.find_element(By.ID, 'gender-radio-1')
    gender.click()

    phone = driver_chrome.find_element(By.ID, 'userNumber')
    phone.send_keys('1234567890')

    date_of_birth = driver_chrome.find_element(By.ID, 'dateOfBirthInput')
    driver_chrome.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", date_of_birth)
    driver_chrome.execute_script("arguments[0].click();", date_of_birth)
    select = Select(driver_chrome.find_element(By.CLASS_NAME, 'react-datepicker__month-select'))
    select.select_by_visible_text("December")
    select = Select(driver_chrome.find_element(By.CLASS_NAME, 'react-datepicker__year-select'))
    select.select_by_visible_text("1900")
    date = driver_chrome.find_element(By.CSS_SELECTOR, '.react-datepicker__day.react-datepicker__day--010')
    date.click()

    subjects = driver_chrome.find_element(By.ID, 'subjectsInput')
    subjects.send_keys("Maths")
    subjects.send_keys(Keys.ENTER)
    subjects.send_keys("Arts")
    subjects.send_keys(Keys.ENTER)

    hobby = driver_chrome.find_element(By.ID, 'hobbies-checkbox-1')
    # листаем что бы нужный чекбокс был в центре
    driver_chrome.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", hobby)
    # жмем не через click а через js, со страницей какая то лабуда click все ломает
    driver_chrome.execute_script("arguments[0].click();", hobby)

    address = driver_chrome.find_element(By.ID, 'currentAddress')
    address.send_keys("Kazan")

    state = driver_chrome.find_element(By.ID, 'react-select-3-input')
    state.send_keys("NCR")
    state.send_keys(Keys.ENTER)

    city = driver_chrome.find_element(By.ID, 'react-select-4-input')
    city.send_keys("Delhi")
    city.send_keys(Keys.ENTER)

    button = driver_chrome.find_element(By.ID, 'submit')
    driver_chrome.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", button)
    driver_chrome.execute_script("arguments[0].click();", button)

    table = driver_chrome.find_element(By.CLASS_NAME, 'table')
    # тут то находит то не находит, на всякий случай закинул ожидание
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'table')))
    print(table.text)
