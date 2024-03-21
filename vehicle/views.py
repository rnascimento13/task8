from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Vehicle


def get_vehicle(request, pk):
    data = get_object_or_404(Vehicle, pk=pk)
    responseData = [
        {
            'brand': data.model.brand.name,
            'model': data.model.name,
            'year': data.year,
            'color': data.color.name,
            'purchase_year': data.purchase_year,
            'condition': data.condition.name,
        }
    ]
    return JsonResponse(responseData, safe=False)
