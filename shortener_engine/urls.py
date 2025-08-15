from django.urls import path
from .views import URLView

urlpatterns = [
    path('shorten/', URLView.as_view(), name='shorten_url'),
]
