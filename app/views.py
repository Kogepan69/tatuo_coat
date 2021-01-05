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

class ReservationView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/reservation.html')

class WashView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/wash.html')

class CoatingView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/coating.html')

class PolishingView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/polishing.html')

class DiagnosisView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/diagnosis.html')

class ProgramView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/program.html')

class CampanyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/campany.html')