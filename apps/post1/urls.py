from django.urls import path
from . import views

app_name = "post"
urlpatterns = [
    path('', views.Home, name="blog-home"),  
    path('about/', views.PostAbout, name="about"),  
    path('blogs/', views.PostListView, name="blogs"), 
    path('post/<slug:slug>/', views.PostDetailView, name="blog"),
    path('post/not-found/', views.NotFound, name="not-found"), 
    path('contact-us/', views.Contact, name="contact"), 
    path('post/cat/<slug:slug>/', views.CategoryListView, name="category"),
    path('post/post-detail/<slug:slug>/update', views.PostUpdateView, name="blog-update"),
    path('post/post-detail/<slug:slug>/delete', views.PostDeleteView, name="blog-delete"),
    path('search/', views.SearchBar, name="search"),
]
