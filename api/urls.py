from django.urls import path
from .views import ShortenURLAPIView, RedirectURLAPIView

urlpatterns = [
    path('shorten/', ShortenURLAPIView.as_view(), name='shorten_url'),
    path('<str:short_code>/', RedirectURLAPIView.as_view(), name='redirect_url'),
]
