from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import ProductionLog

class OEECalculationTests(APITestCase):
    def test_get_production_logs(self):
        url = reverse('oee-calculation')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_production_log(self):
        url = reverse('oee-calculation')
        data = {
            'available_time': 480.0,
            'unplanned_downtime': 20.0,
            'ideal_cycle_time': 5.0,
            'no_of_products': 100,
            'no_of_good_products': 95,
            'cycle_no': '12345',
            'material_name': 'Example Material',
            'machine': 1,
            'start_time': '2024-04-25T10:00:00Z',
            'end_time': '2024-04-25T11:00:00Z',
            'duration': 60,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProductionLog.objects.count(), 1)
        self.assertEqual(ProductionLog.objects.get().cycle_no, '12345')
