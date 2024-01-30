from django.urls import path
from  . import views
urlpatterns = [
    path("blog/create", views.BlogCreateAPIView.as_view() , name="blog_create"),
    path("blog/list",views.BlogListApiview.as_view() , name="blog_list"),
    path("blog/<pk>/edit",views.BlogEditApiview.as_view() , name="blog_Edit"),
    path("blog/<pk>/delete",views.BLogDeleteApiView().as_view(), name="delete"),
    
    path("comment/create", views.CreateComment.as_view() , name="comment_create"),
    path("comment/list",views.ListComment.as_view() , name="comment_list"),
    
]
