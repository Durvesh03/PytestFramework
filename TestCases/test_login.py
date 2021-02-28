import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationUserName()
    password = ReadConfig.getApplicationPassword()

    logger = LogGen.loggens()

    @pytest.mark.regression
    def test_homepageTitle(self, setup):
        self.logger.info("*********** Test_001_Login ***********")
        self.logger.info("*********** Verifying Home Page Title ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login23":
            assert True
            self.logger.info("*********** Home Page Title test is passed ***********")
            self.driver.close()
        else:
            self.driver.save_screenshot("C:\\Users\\durve\\PycharmProjects\\PytestFramework\\Screenshots\\" + "test_homepageTitle.png")
            self.logger.error("*********** Home Page Title test is failed ***********")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, setup):

        self.logger.info("*********** Test_001_Login ***********")
        self.logger.info("*********** Verifying Login Title ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("*********** Login Title test is passed ***********")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\durve\\PycharmProjects\\PytestFramework\\Screenshots\\"+ "test_Login.png")
            self.logger.error("*********** Login Title test is failed ***********")
            self.driver.close()
            assert False

