from django.shortcuts import render
from sale.models import Realty, Garage, Parking, Warehouse, Office, Trade, Industrial, Flat, House


def real_estate_search(request):
    if request.method == 'GET':
        search_query = request.GET.get('search')
        results = []

        if search_query:
            models_to_search = [Garage, Parking, Warehouse, Office, Trade, Industrial, Flat, House]

            for model in models_to_search:
                objects = model.objects.filter(title__icontains=search_query)
                results.extend(objects)

        return render(request, 'real_estate_search.html', {'results': results})

    return render(request, 'real_estate_search.html')
