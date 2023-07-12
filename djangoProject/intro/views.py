from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('<h1>Hello World!</h1>')


@login_required()
# @permission_required('app_label.codename') # pentru restictionarea acesului care lista
def cars(request):
    list_cars = {
        'cars': [
            {
                'brand': 'Toyota',
                'model': 'Land Cruiser',
                'year': 2023
            },
            {
                'brand': 'Mercedes',
                'model': 'GLE-Klasse 63AMG',
                'year': 2023
            },
            {
                'brand': 'Dacia',
                'model': 'Spring',
                'year': 2024
            }
        ]
    }

    return render(request, 'intro/list_of_cars.html', list_cars)


# Exetcitiu
@login_required()
def phones(request):
    list_of_phones = {
        'phones': [
            {
                'brand': 'Apple',
                'model': 'iPhone 14 Pro Max',
                'release': 2023
            },
            {
                'brand': 'Samsung',
                'model': 'S23 Ultra',
                'release': 2022
            },
            {
                'brand': 'Huawei',
                'model': 'HUAWEI P60 Pro 8',
                'release': 2023
            }
        ]
    }

    return render(request, 'intro/list_of_phones.html', list_of_phones)
