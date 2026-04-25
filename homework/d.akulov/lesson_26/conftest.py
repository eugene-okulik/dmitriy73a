from selenium import webdriver
import pytest


@pytest.fixture()
def driver_chromee():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
