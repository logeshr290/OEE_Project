# OEE Calculator Project

This is a Django REST API project for calculating Overall Equipment Effectiveness (OEE) in manufacturing.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/logeshr290/oee_project.git
2. Navigate to the project directory: cd oee_project
3. Create a virtual environment: python -m venv venv
4. Activate the virtual environment: venv\Scripts\activate
5.Install the dependencies: pip install -r requirements.txt

## Usage

1.Run the Django development server: python manage.py runserver
2.Open your browser and go to http://localhost:8000 to access the API.
3.Use tools like Postman or cURL to make POST requests to calculate OEE:
Endpoint: /api/oee-calculation/
Method: POST
Content-Type: application/json
Example JSON input:
json:
{
    "cycle_no": "12345",
    "material_name": "Example Material",
    "start_time": "2024-04-25T10:00:00Z",
    "end_time": "2024-04-25T11:00:00Z",
    "duration": 60,
    "machine": 1,
    "available_time": 480.0,
    "unplanned_downtime": 20.0,
    "ideal_cycle_time": 5.0,
    "no_of_products": 100,
    "no_of_good_products": 95,
    "oee_result": 92.0
}
4.The API will calculate the OEE and return the result in the response.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.
