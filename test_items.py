from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_cart_btn(browser):
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
