from django.urls import path

from measurement.views import DemoView, SensorView



urlpatterns = [
    path('demo/', DemoView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
