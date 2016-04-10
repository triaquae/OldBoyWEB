"""OldboyWebSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from web import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home_page'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^teachers/$', views.teachers, name='teachers'),
    url(r'^course/$', views.course, name='course'),
    url(r'^jobs/$', views.jobs, name='jobs'),
    url(r'^course/py_devops/$', views.course_py_devops, name="course_py_devops"),
    url(r'^course/py_ops/$', views.course_py_ops, name="course_py_ops"),
    url(r'^course/linux_ops/$', views.course_linux_ops, name="course_linux_ops"),
    url(r'^course/linux_architect/$', views.course_linux_architect, name="linux_architect"),
    url(r'^course/bigdata/$', views.course_bigdata, name="bigdata"),
    url(r'^course/enrollment/$', views.how_to_enroll, name="how_to_enroll"),
    url(r'^course/enrollment/(\w+)/$', views.enroll_pages, name="enroll_pages"),
]
