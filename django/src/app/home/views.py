from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html", {"message": "hello"})
