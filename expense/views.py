from rest_framework import generics
from .models import expense
from .serializers import ExpenseSerializer


class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = expense.objects.all()
    serializer_class = ExpenseSerializer
