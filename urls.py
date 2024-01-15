# credit_approval_system/urls.py

from django.contrib import admin
from django.urls import path, include
from django.urls import path
from credit_approval.views import RegisterCustomer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('credit_approval.urls')),
    path('register/', RegisterCustomer.as_view(), name='register-customer')

]
