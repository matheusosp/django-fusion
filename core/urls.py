from django.urls import path
from .views import IndexView, View404

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]