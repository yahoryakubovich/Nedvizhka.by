from django.views.generic import *
from django.shortcuts import get_object_or_404
from .models import *


class FlatListView(ListView):
    model = Flat


class FlatDetailView(DetailView):
    model = Flat
    template_name = "flatdetailview.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
