from django.views.generic import View, TemplateView
from django.shortcuts import render
from .models import Blog,Car
from .forms import CarForm
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html')

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "app/index.html"
    login_url = '/accounts/login/'

class ServiceView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/service.html')

class PriceView(View):
    def get(self, request, *args, **kwargs):
        form = CarForm(request.POST or None)
        return render(request, 'app/price.html', {
        'form': form,
        'price':0
    })
    def post(self, request, *args, **kwargs):
        form = CarForm(request.POST or None)
        

        if form.is_valid():
            car_name= form.cleaned_data['name']
            car_data=Car.objects.get(name=car_name)
            if car_data.size =="SS":
              price=14500

            elif car_data.size =="S":
              price=16000
            
            elif car_data.size =="M":
              price=17500

            elif car_data.size =="L":
              price=19000

            elif car_data.size =="LL":
              price=21500

            elif car_data.size =="XL":
              price=23000

            else:
              price=5000
            print(car_data.size)
            if request.POST.get('iron') == '1':
              price+=1500
            if request.POST.get('water') == '2':
              price+=1500
        

        return render(request, 'app/price.html', {
            'form': form,
            "price":price
        })



class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/contact.html')

class BlogView(View):
    def get(self, request, *args, **kwargs):
        blog_data = Blog.objects.order_by("-id")
        return render(request, 'app/blog.html', {
            'blog_data': blog_data
        })

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

class DetailView(View):
    def get(self, request, *args, **kwargs):
        blog_data = Blog.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/detail.html', {
            'blog_data': blog_data
        })

