from django.core.paginator import Paginator
from django.shortcuts import render
from .models import AllCountryStats
from django.http import JsonResponse


def arrivals_paginated(request):
    print("arrivals_paginated")
    arrivals_list = AllCountryStats.objects.all()
    paginator = Paginator(arrivals_list, 10)  # Show 10 arrivals per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    
    return render(request, 'allcountry_arrivals/index.html', {'page_obj': page_obj})


def get_all_arrivals(request):
    print("get_all_arrivals")
    arrivals_list = AllCountryStats.objects.all()
    data = list(arrivals_list.values())
    print(data)
    return JsonResponse({'results': data}, safe=False)


def country_arrivals_view(request, country_name):
    # Query the database for arrivals by country, excluding 'Total'
    arrivals = AllCountryStats.objects.filter(country__iexact=country_name).exclude(country__iexact='Total')

    # Prepare data for the chart
    chart_data = {
        'labels': [],
        'data': []
    }

    for arrival in arrivals:
        label = f"{arrival.month} {arrival.year}"
        chart_data['labels'].append(label)
        chart_data['data'].append(arrival.passengers)

    return JsonResponse(chart_data)


def country_arrival_page(request):
    return render(request, 'allcountry_arrivals/country_chart.html')