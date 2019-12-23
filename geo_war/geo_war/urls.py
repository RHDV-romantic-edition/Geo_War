from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView


urlpatterns = [   
    path('admin/', admin.site.urls),
    path('map/', include('paiting_map.urls')),
    path('', RedirectView.as_view(url='/map/', permanent=True)),
]