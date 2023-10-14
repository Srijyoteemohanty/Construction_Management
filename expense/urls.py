from django.urls import path


from .views import ExpenseDetailView, ExpenseListCreateView

urlpatterns = [
    path('expense/', ExpenseDetailView.as_view(), name='expense-list-create'),
    path('expense/<int:pk>/', ExpenseListCreateView.as_view(), name='expense-detail'),
]