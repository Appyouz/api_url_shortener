from django.urls import path
from .views import URLView,ShortUrlView
from .import views

urlpatterns = [
    path('shorten/', views.URLView.as_view(), name='shorten_url'),
    path('<str:short_key>/', views.ShortUrlView.as_view(), name='redirect'),
]
