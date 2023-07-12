from html import escape
from pprint import pprint

from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from home.models import Product
import bs4
import requests


class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'


"""
    TemplateView -> este o clasa folosita pentru a afisa un template(o pagina html)
    Proprietatea template_name este folosita pentru a trece calea absoluta catre html
    In concluzie, TemplateView este folosit pentru a afisa un template HTML avand si metode specifice acestui view generic
"""


def get_data_by_emag(request):
    url = 'https://www.emag.ro/televizoare/c?ref=hp_menu_quick-nav_190_1&type=category'
    result = requests.get(url)  # verificam HTTP STATUSul paginii
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    content = {'data': []}
    cases = soup.find_all('div', class_='card-v2')

    for case in cases:
        details_product = {}

        product_title = case.find('a', class_='card-v2-title semibold mrg-btm-xxs js-product-url')
        product_price = case.find('p', class_='product-new-price')

        if product_title is None:
            details_product['title'] = 'No data'
        else:
            details_product['title'] = escape(product_title.text)

        if product_price is None:
            details_product['price'] = 'No data'
        else:
            details_product['price'] = escape(product_price.text)

        content['data'].append(details_product)

    for product in content['data']:
        Product.objects.create(name=product['title'], price=product['price'])

    return redirect('home_page')
