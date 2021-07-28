from django.conf.urls import url,include

from base_app import views


app_name = 'base_app'

urlpatterns = [
    url('relative/',views.relative,name='relative'),
    url('others/',views.others,name='others'),
]
