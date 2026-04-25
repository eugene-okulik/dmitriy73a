from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_1(driver_chromee):
    driver_chromee.get("http://testshop.qa-practice.com/")
    wait = WebDriverWait(driver_chromee, 5)

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'o_wsale_products_item_title')))
    product = driver_chromee.find_elements(By.CLASS_NAME, 'o_wsale_products_item_title')[0]
    text_product = driver_chromee.find_elements(By.CLASS_NAME, 'o_wsale_products_item_title')[0].text

    action = ActionChains(driver_chromee)
    action.key_down(Keys.CONTROL).click(product).key_up(Keys.CONTROL).perform()

    driver_chromee.switch_to.window(driver_chromee.window_handles[1])

    driver_chromee.find_element(By.ID, "add_to_cart").click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-secondary")))
    driver_chromee.find_element(By.CSS_SELECTOR, ".btn.btn-secondary").click()

    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.my_cart_quantity'), "1"))
    driver_chromee.close()

    driver_chromee.switch_to.window(driver_chromee.window_handles[0])

    driver_chromee.find_element(By.CSS_SELECTOR, ".fa.fa-shopping-cart.fa-stack").click()

    assert text_product in driver_chromee.find_element(By.CLASS_NAME, "d-inline").text


def test_2_var1(driver_chromee):
    # оказалось ActionChains не так уж и нужен)
    wait = WebDriverWait(driver_chromee, 5)
    driver_chromee.get("http://testshop.qa-practice.com/")

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'o_wsale_products_item_title')))
    text_product = driver_chromee.find_elements(By.CLASS_NAME, 'o_wsale_products_item_title')[0].text

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "o_wsale_product_btn")))
    driver_chromee.find_elements(By.CLASS_NAME, "o_wsale_product_btn")[0].click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-name")))
    assert text_product in driver_chromee.find_element(By.CLASS_NAME, "product-name").text


def test_2_var2(driver_chromee):
    wait = WebDriverWait(driver_chromee, 5)
    driver_chromee.get("http://testshop.qa-practice.com/")

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'o_wsale_products_item_title')))
    text_product = driver_chromee.find_elements(By.CLASS_NAME, 'o_wsale_products_item_title')[0].text

    product = driver_chromee.find_elements(By.CLASS_NAME, 'oe_product_image')[0]
    btn = driver_chromee.find_elements(By.CLASS_NAME, "o_wsale_product_btn")[0]

    action = ActionChains(driver_chromee)
    action.move_to_element(product)
    action.move_to_element(btn)
    action.click()
    action.perform()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-name")))
    assert text_product in driver_chromee.find_element(By.CLASS_NAME, "product-name").text
