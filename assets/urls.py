from django.urls import path


from .views import AssetDetailView, AssetListCreateView

urlpatterns = [
    path('assets/', AssetDetailView.as_view(), name='assets-list-create'),
    path('assets/<int:pk>/', AssetListCreateView.as_view(), name='assets-detail'),
]