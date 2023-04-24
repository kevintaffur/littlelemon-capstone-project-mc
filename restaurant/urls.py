from django.urls import path
from . import views
# This is another way to get the token (without djoser).
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single_item'),
    path('api-token-auth/', obtain_auth_token),
]