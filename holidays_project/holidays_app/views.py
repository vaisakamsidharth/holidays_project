from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Holiday
from .serializers import HolidaySerializer
import requests

API_KEY = "CALENDARIFIC_API_KEY"
#list all data in listview
class HolidayListView(generics.ListAPIView):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    filterset_fields = ["country"]
    search_fields = ["name"]

#decorator is used for fetch data
@api_view(["GET"])
def fetch_holidays(request, country):
    cache_key = f"holidays_{country}"
    holidays = cache.get(cache_key)

    if not holidays:
        response = requests.get(
            f"https://calendarific.com/api/v2/holidays?api_key={API_KEY}&country={country}&year=2024"

        )
        if response.status_code == 200:  # Check if request is successful
            holidays = response.json().get("response", {}).get("holidays",[])
            cache.set(cache_key,holidays,timeout=3600)
        
        
            for holiday in holidays:
                Holiday.objects.get_or_create(name=holiday["name"],country=country,date=holiday["date"]["iso"])
        else:
            return Response({"error": "Failed to fetch holidays"}, status=response.status_code)

            
    return Response({"holidays":holidays})
