from django.conf.urls import patterns, include, url
from courses.views import *
from django.views.generic import TemplateView

urlpatterns = patterns('',

    # Student
    url(r'^student/create', Student.create_student),
    url(r'^student/login', Student.login),
    url(r'^student/profile/(\d+)$', Student.show_student),
    url(r'^student/profile/$', Student.show_student),

    url(r'^group/create', Group.create_grade_group),
    url(r'^group/list', Group.group_list),
    url(r'^group/profile/(\d+)$', Group.show_group),
)
