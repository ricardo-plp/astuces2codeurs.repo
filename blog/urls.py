from django.urls import path

from blog.views import post

from blog.views import post_detail

urlpatterns = [
    path('',post,name='home_page'),
    path('<slug>/',post_detail,name='detail_post')
]