from django.views.generic import View
from django.shortcuts import render
from .models import Post


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html')

class ServiceView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/service.html')

class PriceView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/price.html')

class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/contact.html')

class BlogView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/blog.html')