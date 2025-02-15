
from django.urls import path
from .views import HolidayListView,fetch_holidays

urlpatterns = [
    path("holidays/" , HolidayListView.as_view(),name ="holidays"),
    path("fetch_holidays/<str:country>/", fetch_holidays,name = "fetch_holidays"),
]