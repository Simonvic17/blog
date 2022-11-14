from django.urls import re_path

from . import views

app_name = "pdf"
urlpatterns = [
    re_path('showposts', views.show_posts, name="showposts"),
    re_path('create-pdf', views.pdf_report_create, name="create-pdf"),
]
