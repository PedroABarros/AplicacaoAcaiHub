from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AcaiHub.urls')),
    path('acaiAuth/', include('acaiAuth.urls'))
]
