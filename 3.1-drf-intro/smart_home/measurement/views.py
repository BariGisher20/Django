from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer


# @api_view(['GET', 'POST'])
# def demo(request):
#     if request.method == 'GET':
#         sensors = Sensor.objects.all()
#         data = SensorSerializer(sensors, many=True)
#         return Response(data.data)
#     if request.method == 'POST':
#         return Response({'status': 'OK'})


# class DemoView(APIView):
#     def get(self, request):
#         sensors = Sensor.objects.all()
#         data = SensorSerializer(sensors, many=True)
#         return Response(data.data)
#
#     def post(self, request):
#         return Response({'status': 'OK'})
# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


class DemoView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        return Response({'status': 'OK'})


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
