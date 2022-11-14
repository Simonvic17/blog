from django.contrib import admin
from django.db import models
from .models import Post, Category, AboutUs
from tinymce.widgets import TinyMCE


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','user')
    list_display_links = ('id', 'title','user')
    list_filter = ['category']
    search_fields = ('title', 'post')
    list_per_page = 25
    formfield_overrides = {models.TextField: {'widget': TinyMCE()}
   }

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(AboutUs)
