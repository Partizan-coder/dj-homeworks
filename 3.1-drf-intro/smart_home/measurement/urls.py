from django.urls import path
from measurement.views import SensorsView, SensorView, MeasurementView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorsView.as_view()),
    path('sensor/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),

]
