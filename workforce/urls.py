from django.urls import path


from .views import WorkforceDetailView, WorkforceListCreateView

urlpatterns = [
    path('workforce/', WorkforceDetailView.as_view(), name='workforce-list-create'),
    path('workforce/<int:pk>/', WorkforceListCreateView.as_view(), name='workforce-detail'),
]

#http://127.0.0.1:8000/api/workforce/1/