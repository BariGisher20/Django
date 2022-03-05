import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


with open('data-398-2018-08-30.csv', 'r', encoding='utf-8') as file:
    directions = list(csv.DictReader(file, delimiter=','))


def bus_stations(request):
    page_number = request.GET.get("page", 1)
    paginator = Paginator(directions, 1)
    page = paginator.get_page(page_number)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    context = {
        'page': page,
        'bus_stations': directions,

    }
    return render(request, 'stations/index.html', context)
