from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.visualize,name = 'visualize'),
    url('^today/$',views.pic_day,name='picsToday')
]
