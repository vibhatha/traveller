"""
URL configuration for traveller_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from touristats import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("allcountry_arrivals/", views.arrivals_paginated, name="allcountry_arrivals"),
    path("allcountry_arrivals/get_all_arrivals/", views.get_all_arrivals, name="get_all_arrivals"),
    path(
        "allcountry_arrivals/<str:country_name>/",
        views.country_arrivals_view,
        name="country_arrivals_json",
    ),
    path(
        "allcountry_arrivals/country_arrival_page/",
        views.country_arrival_page,
        name="country_arrival_page",
    ),
]
