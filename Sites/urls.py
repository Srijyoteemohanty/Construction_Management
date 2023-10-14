from django.urls import path


from .views import SiteDetailView, SiteListCreateView

urlpatterns = [
    path('sites/', SiteListCreateView.as_view(), name='site-list-create'),
    path('sites/<int:pk>/', SiteDetailView.as_view(), name='site-detail'),
]
#http://127.0.0.1:8000/api/sites/