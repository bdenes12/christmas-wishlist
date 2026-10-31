from django.urls import path

from .views import delete_gift, index

app_name = 'christmas_wishlist_app'
urlpatterns = [
    path('gift/', index, name='index'),
    path('<int:id>/delete/', delete_gift, name='gift-delete'),
 ]