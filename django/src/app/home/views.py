from django.http import HttpResponse
from django.views.generic import TemplateView


class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        response = HttpResponse()
        return response
