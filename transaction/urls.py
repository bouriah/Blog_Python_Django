from django.urls import path
from .views import all_transactions, add_income, add_spent


urlpatterns = [
    #path("transactions/", all_transactions, name="all_transactions"),
    path("list/", all_transactions, name="transaction_list"),
    path("income/", add_income, name="add_income"),
    path("spent/", add_spent, name="add_spent"),
]