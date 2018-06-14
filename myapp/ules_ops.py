# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json
import sys
import os
import time
import random
from random import choice
import rstr
from selenium import webdriver
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from .ules.operate import transfromList, Factory
from .ules.dbresource import DBsource
from .ules.page import WorkLoginPage
from .models import Book,TestCase,TestCaseStep


# Create your views here.
@require_http_methods(["GET"])
def run_testcase(request):
    response = {}
    try:
        testcasestep = TestCaseStep.objects.filter(case_name=request.GET.get('case_name')).order_by('step_order')
        testcase = TestCase.objects.filter(case_name=request.GET.get('case_name'))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    print(len(testcasestep))
    for i in testcasestep.values():
        print(i)
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
#     driver.get("https://work-test.1688.com")
    driver.get("https://work.1688.com")
    time.sleep(3)
    print(driver.current_url)
    time.sleep(2)
    workloginpage = WorkLoginPage(driver)
    workloginpage.login()
    time.sleep(3)
    driver.get(testcase.values()[0]["url"])
    args_dics = transfromList(testcasestep.values())
    print(args_dics)
    time.sleep(2)
    factory = Factory()
    for args_dic in args_dics:
        print(args_dic)
        time.sleep(3)
        a = factory.getOps(driver, args_dic)
        a.operate(args_dic)
        #转换为其他日期格式,如:"%Y%m%d_%H_%M_%S"
        driver.get_screenshot_as_file('/Users/jiangwen/Documents/John/work/projects/python/django/pics/'+args_dic["step_name"]+time.strftime("%Y%m%d_%H_%M_%S", time.localtime(int(time.time())))+'.png')
    time.sleep(10)
    driver.close()
    return JsonResponse(response)
