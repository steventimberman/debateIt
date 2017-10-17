#masterDebater URL Configuration

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'debate/', include('debate.urls')),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^blog/comments/', include('fluent_comments.urls')),
    url(r'^comments/', include('django_comments.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
