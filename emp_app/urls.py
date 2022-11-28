from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('add_emp/', add_emp),
    path('delete_emp/<int:emp_id>', delete_emp),
    path('update_emp/<int:emp_id>', update_emp),
    path('filter_emp/', filter_emp)
]