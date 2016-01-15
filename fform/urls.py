from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post, name='post'),
    url(r'^post/$',views.post_list, name='post_list'),
    url(r'^postnew/$', views.post_new, name='post_new')
]
