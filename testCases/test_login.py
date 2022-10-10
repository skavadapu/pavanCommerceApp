import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from testCases.conftest import *
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen


class Test_001_Login:
    # reading the data from config.ini and readProperties.py
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # verify the title of the page
    def test_homePageTitle(self, setup):
        self.logger.info('******************Test_001_Login execution starts************')
        self.logger.info('******************Verifying Home Page Title************')
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            self.driver.close()
            assert True
            self.logger.info('******************Home Page Title Test Passed************')

        else:
            # self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False
            self.logger.error('******************Home Page Title Test Failed************')

    def test_loginJourney(self, setup):
        # setup is fixture which is mentioned in conftest.py
        self.driver = setup
        self.driver.get(self.baseURL)

        #         create the object of LoginPage
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True

        else:
            # self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            assert False
