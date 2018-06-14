#!/anaconda3/bin/python3.6
# coding=utf-8
'''
Created on 2018年5月6日

@author: jiangwen
'''

from .element import BasePageElement
from .locators import MainPageLocators
# from .operate import Factory
import time
from random import choice
from .dbresource import DBsource
import MySQLdb


class SearchTextElement(BasePageElement):
    def __init__(self, element='q'):
        self.locator = element

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver

        

class MainPage(BasePage):
    search_text_element = SearchTextElement()
    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()
  
class WorkLoginPage(BasePage):
    search_text_element = SearchTextElement("TPL_username")
    
    def is_title_matches(self):
        return "1688" in self.driver.title

    def is_results_found(self):
        return "No results found." not in self.driver.page_source
    
    def click_button_switch_login(self,page_id = "J_Quick2Static"):
        """Triggers the search"""
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        self.driver.find_element_by_id("J_Quick2Static").click()
        
    def login(self):
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        if "work-test" in self.driver.current_url:
#             self.driver.find_element_by_id("J_Quick2Static").click()
            self.driver.find_element_by_id("TPL_username_1").send_keys("foxtest001")
            time.sleep(1)
            self.driver.find_element_by_id("TPL_password_1").send_keys("taobao1234")
            self.driver.find_element(*MainPageLocators.GO_BUTTON).click()
        elif "work.1688" in self.driver.current_url:
            self.driver.find_element_by_id("J_Quick2Static").click()
            self.driver.find_element_by_id("TPL_username_1").send_keys("dongyl1111")
            time.sleep(1)
            self.driver.find_element_by_id("TPL_password_1").send_keys("1111112")
            self.driver.find_element(*MainPageLocators.GO_BUTTON).click()
        else:
            print("url error")
    
    def addMember(self,args_dic):
        pass
    
#     def addEmployee(self,args_dic):
#         pass 
        
    def addEmployee(self,args_dic):
        self.driver.get("http://cgjc-test.1688.com/page/organization?log=true")
#         self.driver.find_element_by_css_selector(".next-btn-primary").click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//span/button[@type="button" and contains(@class,"next-btn-primary")]').click()
        time.sleep(1)
        self.driver.find_element_by_id('name').send_keys("haha")
        time.sleep(1)
        self.driver.find_element_by_xpath('//span/input[@type="radio" and @value="2"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//span/input[@type="text" and @placeholder="请输入账号名"]').send_keys("haha")
        time.sleep(1)
        self.driver.find_element_by_xpath('//span/input[@type="password" and @placeholder="由数字与字母组成6～16的字符"]').send_keys("123456")
        time.sleep(1)
        self.driver.find_element_by_xpath('//span/input[@type="password" and @placeholder="请重复再输一遍"]').send_keys("123456")
        time.sleep(1)
        self.driver.find_element_by_xpath('//span/span[@class="next-select-inner"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//li/a[@class="next-tree-node-handle"]').click()
        time.sleep(1)
        self.driver.find_element_by_id('securityPhone').send_keys("14755667788")
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@label="职务" and contains(@class,next-form-item)]/div/span/span[@class="next-select-inner"]').click()
        time.sleep(1)
        choice(self.driver.find_elements_by_xpath('//ul[@class="next-menu-content"]/li')).click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@label="岗位" and contains(@class,next-form-item)]/div/span/span[@class="next-select-inner"]').click()
        time.sleep(1)
        choice(self.driver.find_elements_by_xpath('//ul[@class="next-menu-content"]/li')).click()
        time.sleep(1)
        self.driver.find_element_by_id('employeeNumber').send_keys("haha11")
        time.sleep(1)
        self.driver.find_element_by_id('nickName').send_keys("haha22")
        time.sleep(1)
        self.driver.find_element_by_id('personalMobilePhone').send_keys("13455667788")
        time.sleep(1)
        self.driver.find_element_by_id('email').send_keys("haha@gg.com")
        time.sleep(1)
        self.driver.find_element_by_id('fixedPhone').send_keys("0571-88776655")
        time.sleep(1)
        self.driver.find_element_by_id('workLocation').send_keys("杭州")
        time.sleep(5)

    
    def create_custom_sheet(self,args_dic):
        self.driver.get("http://cgcm.1688.com/custom/report/myreport.htm")
        self.driver.find_element_by_css_selector(".mychart-newreport-btn").click()
        self.driver.find_element_by_id("input-report-name").send_keys(args_dic["name"])
#         custom_report_groups_fields_list = self.driver.find_elements_by_css_selector("custom-report-groups-fields-list-item")
#         print("**1**")
        custom_report_groups_fields_list = self.driver.find_elements_by_xpath('//span/span[@class="custom-report-groups-fields-list-item-icon"]')
        print("**2**")
        print(len(custom_report_groups_fields_list))
#         custom_report_groups_fields_list[0].xpath()
        flag = True
        for item in custom_report_groups_fields_list[1:]:
            print(item.find_element_by_xpath('./i[@class="iconfont"]'))
            print(item.find_element_by_xpath('../span[@class="custom-report-groups-fields-list-item-text"]').text )
            if (item.find_element_by_xpath('../span[@class="custom-report-groups-fields-list-item-text"]').text in ["是否含税","询价截止时间","报价通过数量"\
                                                                                                                    ,"询价单状态","询价方式","采购类型"\
                                                                                                                    ,"比价方式","业务日期"]) and flag:
                flag = not flag
                continue
            else:
                flag = True
            item.click()
            time.sleep(1)
        secondary_button = self.driver.find_elements_by_xpath('//button[@type="button"][contains(@class, "secondary")]')
        print("**3**")
        print(len(secondary_button))
        secondary_button[-1].click()
        time.sleep(1)
        
if __name__ == "__main__":
    print("page.py")