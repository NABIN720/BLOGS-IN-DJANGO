from django.urls import path
from . import views


urlpatterns = [
    # path('', views.blog_list, name='blog_list'),                  # For blog listing
    # path('post/<slug:slug>/', views.blog_detail, name='blog_detail'),  # For individual post details
    path('',views.index,name='index'),
    path('blogpost/<int:id>/',views.post,name='blogPost')
] 

    
