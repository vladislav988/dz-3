import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV





def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    dic = []
    with open(BUS_STATION_CSV, encoding='utf-8') as csvfile:
        page_number = request.GET.get("page", 1)
        reader = csv.DictReader(csvfile)
        for i in reader:
            a = [{
                "Street": i["Street"],
                "Name": i["Name"],
                "District": i["District"]}]
            dic += a
        print(dic)


        pagi = Paginator(dic, 10)
        pagi_1 = pagi.get_page(page_number)
        print(str(page_number))

        context = {
            "bus_stations":  pagi_1,
            "page_number": page_number
        }

    return render(request, 'stations/index.html', context)
