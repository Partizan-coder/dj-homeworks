from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer

class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        sensorSer = SensorSerializer(data=request.data)
        if sensorSer.is_valid():
            sensorSer.save()
        return Response({'status': 'OK, data posted successfully'})

    def patch(self, request, pk, 'ep111'):
        sensor = Sensor.objects.get(pk)
        requestData = request.data
        print(requestData)
        sensorSer = SensorSerializer(sensor, data=request.data)
        if sensorSer.is_valid():
            sensorSer.save()
        return Response({'status': 'OK, data patched successfully'})


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        maesurementSer = MeasurementSerializer(data=request.data)
        if maesurementSer.is_valid():
            maesurementSer.save()
        return Response({'status': 'OK, data posted successfully'})
