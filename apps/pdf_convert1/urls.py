from django.urls import path

from . import views

app_name = "pdf"
urlpatterns = [
    path('showposts', views.show_posts, name="showposts"),
    path('create-pdf', views.pdf_report_create, name="create-pdf"),
]
