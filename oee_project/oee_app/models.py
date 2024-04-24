from django.db import models
import uuid

class Machine(models.Model):
    machine_name = models.CharField(max_length=100)
    machine_serial_no = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.machine_name

class ProductionLog(models.Model):
    available_time = models.FloatField()
    unplanned_downtime = models.FloatField()
    ideal_cycle_time = models.FloatField()
    no_of_products = models.IntegerField()
    no_of_good_products = models.IntegerField()
    oee_result = models.FloatField()
    cycle_no = models.CharField(max_length=50)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False)
    material_name = models.CharField(max_length=100)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.FloatField()

    def __str__(self):
        return self.cycle_no
