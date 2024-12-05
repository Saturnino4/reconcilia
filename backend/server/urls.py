
from django.urls import path, include, re_path
# from api.views import notFound
from server import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/v1/', include('api.urls')),
    # re_path(r'^.*$', notFound),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
