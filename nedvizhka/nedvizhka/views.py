from django.http import HttpResponse


def index(request):
    return HttpResponse("<a href='http://127.0.0.1:8000/sale/flat/'>Продам гараж жак фреско </a>")
