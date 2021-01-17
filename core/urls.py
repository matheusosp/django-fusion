from django.urls import path
from .views import IndexView
from .views import redirect_view
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login', redirect_view, name="login")
]