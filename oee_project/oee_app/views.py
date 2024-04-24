from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Machine, ProductionLog
from .serializers import MachineSerializer, ProductionLogSerializer


class OEECalculationView(APIView):
    def get(self, request):
        production_logs = ProductionLog.objects.all()
        serializer = ProductionLogSerializer(production_logs, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = ProductionLogSerializer(data=data)
        if serializer.is_valid():
            # Perform OEE calculation here
            available_time = float(data.get('available_time'))
            unplanned_downtime = float(data.get('unplanned_downtime'))
            ideal_cycle_time = float(data.get('ideal_cycle_time'))
            no_of_products = int(data.get('no_of_products'))
            no_of_good_products = int(data.get('no_of_good_products'))

            availability = ((available_time - unplanned_downtime) / available_time) * 100
            available_operating_time = no_of_products * (ideal_cycle_time / 60)
            performance = (ideal_cycle_time * no_of_products) / available_operating_time * 100
            quality = (no_of_good_products / no_of_products) * 100
            oee = availability * performance * quality / 10000

            # Save input data and OEE result to the database
            serializer.save(oee_result=oee)

            # Prepare response data with calculated OEE
            response_data = serializer.data
            response_data['oee'] = oee
            response_data['message'] = 'Data saved successfully'

            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MachineListView(generics.ListAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class ProductionLogListView(generics.ListAPIView):
    queryset = ProductionLog.objects.all()
    serializer_class = ProductionLogSerializer
