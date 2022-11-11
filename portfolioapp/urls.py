from django.urls import path
from .views import PortfolioHomeView

urlpatterns = [
    path('',PortfolioHomeView,name="portfolio-home"),
]