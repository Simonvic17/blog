from django.urls  import include, re_path
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Blog's Admin Panel"
admin.site.site_title = 'BLOG'
admin.site.index_title = 'Welcome to Blog'

urlpatterns = [
    re_path('tinymce/', include('tinymce.urls')),     
    re_path("", include("apps.post.urls")),
    re_path("report/", include("apps.pdf_convert.urls")),
    re_path("user/", include("apps.user.urls")),
    
    re_path('admin/', admin.site.urls),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'apps.post.views.NotFound'
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*', 
                        TemplateView.as_view(template_name='blog/index.html'))]

