from django.urls import path


from .views import SiteDetailView, SiteListCreateView

urlpatterns = [
    path('api/', SiteListCreateView.as_view(), name='site-list-create'),
    path('api/<int:pk>/', SiteDetailView.as_view(), name='site-detail'),
]
