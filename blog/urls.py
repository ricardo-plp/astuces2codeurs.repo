from django.urls import path



from blog.views import post_detail
#from blog.views import Post_Index


from blog.views import post

urlpatterns = [
#    path('',Post_Index.as_view(), name='post_list'),
    path('',post, name='post_list'),
    path('category/<slug:category>/',post,name='category_post'),
    path('<slug>/',post_detail,name='detail_post'),
]