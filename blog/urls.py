from django.urls import path



from blog.views import post_detail
from blog.views import Post_Index

urlpatterns = [
    path('',Post_Index.as_view(), name='post_list'),
    path('<slug>/',post_detail,name='detail_post'),

]