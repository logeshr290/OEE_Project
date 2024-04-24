from django.urls import path
from . import views

urlpatterns = [
    path('machines/', views.MachineListView.as_view(), name='machine-list'),
    path('production-logs/', views.ProductionLogListView.as_view(), name='production-log-list'),
    path('oee-calculation/', views.OEECalculationView.as_view(), name='oee-calculation'),
]
