from django.urls import path
from .views import *

urlpatterns = [
    path('heartrate/', HeartRateListCreateView.as_view(), name='heartrate-list-create'),
    path('heartrate/<int:pk>/', HeartRateRetrieveUpdateDeleteView.as_view(), name='heartrate-detail'),
]
