from rest_framework import serializers
from .models import Machine, ProductionLog

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'

class ProductionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionLog
        fields = '__all__'
