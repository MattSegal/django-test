from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from . import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^people/', include('people.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
