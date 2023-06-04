from django.urls import path
from measurement.views import CreateSensorView, UpdateSensorView, MeasurementView

urlpatterns = [
    path('sensors/<int:pk>/', UpdateSensorView.as_view()),
    path('sensors/', CreateSensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('sensor/<int:pk>/', UpdateSensorView.as_view())
]
