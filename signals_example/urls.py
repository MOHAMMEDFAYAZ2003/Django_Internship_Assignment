from django.urls import path
from .views import test_signals

urlpatterns = [
    path('test-signals/', test_signals, name='test_signals'),
]
