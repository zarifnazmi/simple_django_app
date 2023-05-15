from django.urls import path
from .views import GetScore

urlpatterns = [
    path('get_score/', GetScore.as_view(), name='get_score'),
]
