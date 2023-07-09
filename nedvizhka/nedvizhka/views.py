from django.http import HttpResponse


def index(request):
    return HttpResponse("Здесь будет выведен список объявлений.")
