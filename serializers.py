# credit_approval/serializers.py

from rest_framework import serializers
from credit_approval.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'first_name', 'last_name', 'monthly_salary', 'approved_limit', 'phone_number']
