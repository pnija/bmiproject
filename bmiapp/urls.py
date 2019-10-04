from django.urls import path

from bmiapp.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
]
