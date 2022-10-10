from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome("C:\Automation\Drivers\chromedriver.exe")
    return driver
