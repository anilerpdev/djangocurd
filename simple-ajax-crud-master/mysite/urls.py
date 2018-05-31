from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib import admin

from mysite.books import views
from mysite.student import views1

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^books/$', views.book_list, name='book_list'),
    url(r'^books/create/$', views.book_create, name='book_create'),
    url(r'^books/(?P<pk>\d+)/update/$', views.book_update, name='book_update'),
    url(r'^books/(?P<pk>\d+)/delete/$', views.book_delete, name='book_delete'),

    url(r'^student/$', views1.student_list, name='student_list'),
    url(r'^student/create/$', views1.student_create, name='student_create'),
    url(r'^student/(?P<pk>\d+)/update/$', views1.student_update, name='student_update'),
    url(r'^student/(?P<pk>\d+)/delete/$', views1.student_delete, name='student_delete'),
]
