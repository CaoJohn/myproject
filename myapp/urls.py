from django.conf.urls import url, include
from . import views
from . import ules_ops
#import views

urlpatterns = [
    url(r'add_book$', views.add_book, ),
    url(r'show_books$', views.show_books, ),
    url(r'add_testcase$', views.add_testcase, ),
    url(r'delete_testcase$', views.delete_testcase, ),
    url(r'get_testcase$', views.get_testcase, ),
    url(r'update_testcase$', views.update_testcase, ),
    url(r'get_testcases$', views.get_testcases, ),
    url(r'add_testcasestep$', views.add_testcasestep, ),
    url(r'get_testcasesteps$', views.get_testcasesteps, ),
    url(r'get_testcasestep$', views.get_testcasestep, ),
    url(r'update_testcasestep$', views.update_testcasestep, ),
    url(r'run_testcase$', ules_ops.run_testcase, ),
    ]
