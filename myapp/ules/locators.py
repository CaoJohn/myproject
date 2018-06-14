#!/anaconda3/bin/python3.6
# coding=utf-8
'''
Created on 2018年4月26日

@author: jiangwen
'''

from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'J_SubmitStatic')
    GO_LOGIN_MODE = (By.ID, 'J_Quick2Static')
    GO_LOGIN_MODE1 = (By.CLASS_NAME, 'iconfont static')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass

if __name__ == "__main__":
    print("locaters.py")
    t = MainPageLocators()
    e = t.GO_LOGIN_MODE
    print(*t.GO_LOGIN_MODE)
    print(type(e))
    