from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.authtoken import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('solution.urls')),
                  path('api-auth/', include('rest_framework.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)