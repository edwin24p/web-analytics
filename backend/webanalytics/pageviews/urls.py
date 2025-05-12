from django.urls import path
from .views import PageViewCreateView

urlpatterns = [
    path('log/', PageViewCreateView.as_view(), name='pageview-log'),
    
]