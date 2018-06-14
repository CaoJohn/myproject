#!/usr/bin/env python3
# coding=utf-8
'''
Created on 2018年4月26日

@author: jiangwen
'''
import sys
import os
import time
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from selenium import webdriver
# from .page import MainPage,SearchResultsPage
from membertest.page import WorkLoginPage

if __name__ == "__main__":
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    driver.get("https://work-test.1688.com")
    #转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    otherStyleTime = time.strftime("%m%d%H%M%S", time.localtime(int(time.time())))
    print(otherStyleTime)
    args_dic = {
        "name":"jw_auto_"+otherStyleTime,
        "brandname":"jw_test",
        "brandmodel":"10001",
        "materailcode":"jw_auto_test"+otherStyleTime,
        "unit":(1,2,3)
        }
    print(driver.current_url)
    time.sleep(2)
    workloginpage = WorkLoginPage(driver)
    workloginpage.login()
    time.sleep(5)
    workloginpage.addEmployee(args_dic)
    time.sleep(5)
    driver.close()

