# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json

from .models import Book,TestCase,TestCaseStep

# Create your views here.
@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list']  = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

# Create Testcase views here.
@require_http_methods(["GET"])
def add_testcase(request):
    response = {}
    try:
        testcase = TestCase(case_name=request.GET.get('case_name'))
        testcase.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

# Delete Testcase here.
@require_http_methods(["GET"])
def delete_testcase(request):
    response = {}
    try:
        testcase = TestCase.objects.filter(case_name=request.GET.get('case_name')).delete()
        # testcase.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

# get Testcases here.
@require_http_methods(["GET"])
def get_testcases(request):
    response = {}
    try:
        testcases = TestCase.objects.filter()
        response['list']  = json.loads(serializers.serialize("json", testcases))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

# get Testcase here.
@require_http_methods(["GET"])
def get_testcase(request):
    response = {}
    try:
        testcase = TestCase.objects.filter(case_name=request.GET.get('case_name'),)
        response['list']  = json.loads(serializers.serialize("json", testcase))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# update Testcase here.
@require_http_methods(["GET"])
def update_testcase(request):
    response = {}
    try:
        testcase = TestCase.objects.filter(id=request.GET.get('id')).update(case_name=request.GET.get('case_name'),
                                                    url=request.GET.get('url'))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# Create Testcasestep views here.
@require_http_methods(["GET"])
def add_testcasestep(request):
    response = {}
    try:
        testcasestep = TestCaseStep(step_name=request.GET.get('step_name'),
                                    case_name=request.GET.get('case_name'),
                                    case_id=request.GET.get('case_id'),
                                    step_order=request.GET.get('step_order'),
                                    locator=request.GET.get('locator'),
                                    location=request.GET.get('location'),
                                    type=request.GET.get('type'),
                                    ops=request.GET.get('ops'),
                                    value=request.GET.get('value'),
                                    ret_assert=request.GET.get('ret_assert'),
                                    required=request.GET.get('required'),
                                    ops_detail=request.GET.get('ops_detail'),
                                    pic_address=request.GET.get('pic_address'),
                                    imgdiff=request.GET.get('imgdiff'),
                                    element_type=request.GET.get('element_type'),
                                    reg_type=request.GET.get('reg_type'))
        testcasestep.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

# Create Testcasestep views here.
@require_http_methods(["GET"])
def update_testcasestep(request):
    response = {}
    try:
        testcasestep = TestCaseStep.objects.filter(id=request.GET.get('id')).update(case_name=request.GET.get('case_name'),
                                        case_id=request.GET.get('case_id'),
                                        step_name=request.GET.get('step_name'),
                                        step_order=request.GET.get('step_order'),
                                        locator=request.GET.get('locator'),
                                        location=request.GET.get('location'),
                                        type=request.GET.get('type'),
                                        ops=request.GET.get('ops'),
                                        value=request.GET.get('value'),
                                        ret_assert=request.GET.get('ret_assert'),
                                        required=request.GET.get('required'),
                                        ops_detail=request.GET.get('ops_detail'),
                                        pic_address=request.GET.get('pic_address'),
                                        imgdiff=request.GET.get('imgdiff'),
                                        element_type=request.GET.get('element_type'),
                                        reg_type=request.GET.get('reg_type'))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)



@require_http_methods(["GET"])
def get_testcasesteps(request):
    response = {}
    try:
        testcasesteps = TestCaseStep.objects.filter(case_name=request.GET.get('case_name'))
        response['list']  = json.loads(serializers.serialize("json", testcasesteps))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def get_testcasestep(request):
    response = {}
    try:
        testcasestep = TestCaseStep.objects.filter(case_name=request.GET.get('case_name'),step_name=request.GET.get('step_name'))
        response['list']  = json.loads(serializers.serialize("json", testcasestep))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
