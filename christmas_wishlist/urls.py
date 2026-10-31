from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('gifts/', include('christmas_wishlist_app.urls')),
    path('admin/', admin.site.urls),
]
