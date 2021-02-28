import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGen
from Utilities import XLUtils
import time

class Test_002_DDT_Login:
    path = "C:\\Users\\durve\\PycharmProjects\\PytestFramework\\TestData\\LoginData.xlsx"
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggens()


    @pytest.mark.regression
    def test_Login_DDT(self, setup):

        self.logger.info("*********** Test_002_DDT_Login ***********")
        self.logger.info("*********** Verifying Login Title ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)

        self.rows = XLUtils.getRowCount(self.path,"Sheet1")
        print("Number of rows in excel:", self.rows)
        lst_status = [] # Empty ist variable
        for r in range(2,self.rows + 1):
            self.username = XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.expected = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.expected == "Pass":
                    self.logger.info("*********** Login Title test is passed ***********")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                else:
                    self.driver.save_screenshot("C:\\Users\\durve\\PycharmProjects\\PytestFramework\\Screenshots\\"+ "test_Login.png")
                    self.logger.error("*********** Login Title test is failed ***********")
                    lst_status.append("Fail")
                    self.lp.clickLogout()
            else:
                if self.expected == "Fail":
                    self.logger.info("*********** Login Title test is passed ***********")
                    lst_status.append("Pass")
                else:
                    self.driver.save_screenshot("C:\\Users\\durve\\PycharmProjects\\PytestFramework\\Screenshots\\"+ "test_Login.png")
                    self.logger.error("*********** Login Title test is failed ***********")
                    lst_status.append("Fail")

        if "Fail" not in lst_status:
            self.logger.error("*********** Test Login DDT testcase is passed ***********")
            self.driver.close()
            assert True
        else:
            self.logger.error("*********** Test Login DDT testcase is failed ***********")
            self.driver.close()
            assert False

        self.logger.info("************End of Login Test CAse DDT**************")
        self.logger.info('**************Completed TC_LoginDDT_002**************')