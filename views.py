# credit_approval/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from credit_approval.models import Loan
from credit_approval.serializers import LoanSerializer
from credit_approval.models import Customer
from credit_approval.serializers import CustomerSerializer

class ViewLoan(APIView):
    def get(self, request, loan_id, *args, **kwargs):
        try:
            loan = Loan.objects.get(loan_id=loan_id)
        except Loan.DoesNotExist:
            return Response({'error': 'Loan not found'}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the loan data
        serializer = LoanSerializer(loan)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RegisterCustomer(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data

        # Validate input data
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            # Calculate approved limit based on the given formula
            monthly_salary = data['monthly_salary']
            approved_limit = round(36 * monthly_salary, -5)  # Round to nearest lakh

            # Create a new customer
            customer = Customer.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                monthly_salary=monthly_salary,
                approved_limit=approved_limit,
                phone_number=data['phone_number']
            )

            # Serialize the response data
            response_data = {
                'customer_id': customer.customer_id,
                'name': f"{customer.first_name} {customer.last_name}",
                'age': data.get('age'),
                'monthly_income': monthly_salary,
                'approved_limit': approved_limit,
                'phone_number': data['phone_number'],
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)