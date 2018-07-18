from django.conf.urls import url

from App import views

urlpatterns=[
    url(r'^index/',views.index,name='index'),
    url(r'^userzhu/',views.user_zhuce,name='user_zhuce'),
    url(r'^userlogin/',views.user_login,name='user_login'),
    url(r'^userzhongxin/',views.user_zhongxin,name='user_zhongxin'),
    url(r'^userlogout/',views.user_logout,name='user_logout'),
    url(r'^userinfor/',views.user_infor,name='user_infor')

]