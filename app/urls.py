from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('service/', views.ServiceView.as_view(), name='service'),
    path('price/', views.PriceView.as_view(), name='price'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('reservation/', views.ReservationView.as_view(), name='reservation'),
    path('wash/', views.WashView.as_view(), name='wash'),
    path('coating/', views.CoatingView.as_view(), name='coating'),
    path('polishing/', views.PolishingView.as_view(), name='polishing'),
    path('diagnosis/', views.DiagnosisView.as_view(), name='diagnosis'),
    path('program/', views.ProgramView.as_view(), name='program'),
    path('campany/', views.CampanyView.as_view(), name='campany'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
]