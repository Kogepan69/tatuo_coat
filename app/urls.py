from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('service/', views.ServiceView.as_view(), name='service'),
    path('price/', views.PriceView.as_view(), name='price'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('wash/', views.WashView.as_view(), name='wash'),
    path('coating/', views.CoatingView.as_view(), name='coating'),
    path('polishing/', views.PolishingView.as_view(), name='polishing'),
    path('diagnosis/', views.DiagnosisView.as_view(), name='diagnosis'),
    path('program/', views.ProgramView.as_view(), name='program'),
    path('campany/', views.CampanyView.as_view(), name='campany'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('store', views.StoreView.as_view(), name='store'),
    path('store/<int:pk>/', views.StaffView.as_view(), name='staff'),
    path('calendar/<int:pk>/', views.CalendarView.as_view(), name='calendar'), 
    path('calendar/<int:pk>/<int:year>/<int:month>/<int:day>/', views.CalendarView.as_view(), name='calendar'),
    path('booking/<int:pk>/<int:year>/<int:month>/<int:day>/<int:hour>/', views.BookingView.as_view(), name='booking'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    path('mypage/<int:year>/<int:month>/<int:day>/', views.MyPageView.as_view(), name='mypage'),
    path('mypage/holiday/<int:year>/<int:month>/<int:day>/<int:hour>/', views.Holiday, name='holiday'),
    path('mypage/delete/<int:year>/<int:month>/<int:day>/<int:hour>/', views.Delete, name='delete'),
]