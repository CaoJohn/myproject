#!/anaconda3/bin/python3.6
# coding=utf-8
'''
Created on 2018年5月11日

@author: jiangwen
'''
import sys
import os
import time
import random
from random import choice
import rstr
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from selenium import webdriver
from .dbresource import DBsource
from .page import WorkLoginPage


class BaseOps(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver, args_dic):
        self.driver = driver
        self.args_dic = args_dic
    
    def operate(self,args_dic={}):
        pass

class FindElementByXpath(BaseOps):
    def operate(self, args_dic={}):
        if args_dic["ops"]=="click" and args_dic["type"]=="button":
            self.driver.find_element_by_xpath(args_dic["location"]).click()
        elif args_dic["ops"]=="sendkey" and args_dic["type"]=="input":
            self.driver.find_element_by_xpath(args_dic["location"]).send_keys(args_dic["value"])
        else:
            print("operate type error")

class FindElementByID(BaseOps):
    def operate(self, args_dic={}):
        if args_dic["ops"]=="click" and args_dic["type"]=="button":
            self.driver.find_element_by_id(args_dic["location"]).click()
        elif args_dic["ops"]=="sendkey" and args_dic["type"]=="input":
            self.driver.find_element_by_id(args_dic["location"]).send_keys(args_dic["value"])
        else:
            print("operate type error")

class FindElementByClass(BaseOps):
    def operate(self, args_dic={}):
        if args_dic["ops"]=="click" and args_dic["type"]=="button":
            self.driver.find_element_by_class(args_dic["location"]).click()
        elif args_dic["ops"]=="sendkey" and args_dic["type"]=="input":
            self.driver.find_element_by_class(args_dic["location"]).send_keys(args_dic["value"])
        else:
            print("operate type error")
            
class FindElementByCssSelector(BaseOps):
    def operate(self, args_dic={}):
        if args_dic["ops"]=="click" and args_dic["type"]=="button":
            self.driver.find_element_by_css_selector(args_dic["location"]).click()
        elif args_dic["ops"]=="sendkey" and args_dic["type"]=="input":
            self.driver.find_element_by_css_selector(args_dic["location"]).send_keys(args_dic["value"])
        else:
            print("operate type error")

class FindElementByName(BaseOps):
    def operate(self, args_dic={}):
        if args_dic["ops"]=="click" and args_dic["type"]=="button":
            self.driver.find_element_by_name(args_dic["location"]).click()
        elif args_dic["ops"]=="sendkey" and args_dic["type"]=="input":
            self.driver.find_element_by_name(args_dic["location"]).send_keys(args_dic["value"])
        else:
            print("operate type error")
            
#Elements
class FindElementsByXpath(BaseOps):
    def operate(self, args_dic={}):
        if args_dic["ops"]=="click" and args_dic["type"]=="button":
            choice(self.driver.find_elements_by_xpath(args_dic["location"])).click()

class FindElementsByID(BaseOps):
    def operate(self, args_dic={}):
        if args_dic["ops"]=="click" and args_dic["type"]=="button":
            choice(self.driver.find_elements_by_id(args_dic["location"])).click()
            
class FindElementsByClass(BaseOps):
    def operate(self, args_dic={}):
        if args_dic["ops"]=="click" and args_dic["type"]=="button":
            choice(self.driver.find_elements_by_class(args_dic["location"])).click()
            
class FindElementsByCssSelector(BaseOps):
    def operate(self, args_dic={}):
        if args_dic["ops"]=="click" and args_dic["type"]=="button":
            choice(self.driver.find_elements_by_css_selector(args_dic["location"])).click()

class FindElementsByName(BaseOps):
    def operate(self, args_dic={}):
        if args_dic["ops"]=="click" and args_dic["type"]=="button":
            choice(self.driver.find_elements_by_name(args_dic["location"])).click()
            
class Factory(object):
    def getOps(self, driver,args_dic):
        if args_dic["element_type"]=="basic":
            if args_dic["locator"]=="xpath":
                return FindElementByXpath(driver,args_dic) 
            elif args_dic["locator"]=="class":
                return FindElementByClass(driver,args_dic)
            elif args_dic["locator"]=="id":
                return FindElementByID(driver,args_dic)
            elif args_dic["locator"]=="css_selector":
                return FindElementByCssSelector(driver,args_dic)
            elif args_dic["locator"]=="name":
                return FindElementByName(driver,args_dic) 
            else:
                print("locator error")
        elif args_dic["element_type"]=="list":
            if args_dic["locator"]=="xpath":
                return FindElementsByXpath(driver,args_dic) 
            elif args_dic["locator"]=="class":
                return FindElementsByClass(driver,args_dic)
            elif args_dic["locator"]=="id":
                return FindElementsByID(driver,args_dic)
            elif args_dic["locator"]=="css_selector":
                return FindElementsByCssSelector(driver,args_dic)
            elif args_dic["locator"]=="name":
                return FindElementsByName(driver,args_dic)  
            else:
                print("locator error")
        else:
            print("element type error")

def transfromList(sql_tuples):
    require_dics = []
    no_require_dics = []
    for item in sql_tuples:
        if item["required"]==1:
            if (item["reg_type"]=='' or item["reg_type"]=='no_reg'):
                require_dics.append(item)
            else:
                item["value"] = rstr.xeger(item["reg_type"])
                require_dics.append(item)
        else:
            if (item["reg_type"]=='' or item["reg_type"]=='no_reg'):
                no_require_dics.append(item)
            else:
                item["value"] = rstr.xeger(item["reg_type"])
                no_require_dics.append(item)
        print(item["value"] )
    print(require_dics+no_require_dics)
    return require_dics+random.sample(no_require_dics, random.randint(0,len(no_require_dics)))
        
if __name__ == "__main__":
    mydb = DBsource();
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
#     driver.get("https://work-test.1688.com")
    driver.get("https://work.1688.com")
    time.sleep(3)
    
    print(driver.current_url)
    time.sleep(2)
    workloginpage = WorkLoginPage(driver)
    workloginpage.login()
    time.sleep(3)
#     driver.get("https://cgjc.1688.com/product/newPostProduct.htm")
#     sql = 'select * from selUops where name="caigou_material_create" order by ops_order' #定义查询操作的sql语句
    driver.get("http://cgjc.1688.com/page/organization?log=true")
    sql = 'select * from selUops where name="caigou_member_create" order by ops_order' #定义查询操作的sql语句

    tmp_dic = mydb.getSqlResults(sql)
    print(tmp_dic)
    args_dics = transfromList(tmp_dic)
    time.sleep(2)
    factory = Factory()
    for args_dic in args_dics:
        print(args_dic)
        time.sleep(3)
        a = factory.getOps(driver, args_dic)
        a.operate(args_dic)
    
    time.sleep(10)
    driver.close()
    
      
