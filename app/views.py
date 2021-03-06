from app.models import Store, Staff, Booking
from django.views.generic import View, TemplateView
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Car, Category
from .forms import CarForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import localtime, make_aware
from datetime import datetime, date, timedelta, time
from django.db.models import Q
from app.forms import BookingForm
from django.views.decorators.http import require_POST
import textwrap
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.conf import settings


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html')

class BlogView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by("-id")
        return render(request, 'app/blog.html', {
            'post_data': post_data,
        })

class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/post_detail.html', {
            'post_data': post_data
        })

class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/post_delete.html', {
            'post_data': post_data
        })

    def post(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        post_data.delete()
        return redirect('index')

class CreatePostView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        return render(request, 'app/post_form.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Post()
            post_data.author = request.user
            post_data.title = form.cleaned_data['title']
            category = form.cleaned_data['category']
            category_data = Category.objects.get(name=category)
            post_data.category = category_data
            post_data.content = form.cleaned_data['content']
            if request.FILES:
                post_data.image = request.FILES.get('image')
            post_data.save()
            return redirect('post_detail', post_data.id)

        return render(request, 'app/post_form.html', {
            'form': form
        })


class PostEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        form = PostForm(
            request.POST or None,
            initial={
                'title': post_data.title,
                'category': post_data.category,
                'content': post_data.content,
                'image': post_data.image,
            }
        )

        return render(request, 'app/post_form.html', {
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Post.objects.get(id=self.kwargs['pk'])
            post_data.title = form.cleaned_data['title']
            category = form.cleaned_data['category']
            category_data = Category.objects.get(name=category)
            post_data.category = category_data
            post_data.content = form.cleaned_data['content']
            if request.FILES:
                post_data.image = request.FILES.get('image')
            post_data.save()
            return redirect('post_detail', self.kwargs['pk'])

        return render(request, 'app/post_form.html', {
            'form': form
        })


class CategoryView(View):
    def get(self, request, *args, **kwargs):
        category_data = Category.objects.get(name=self.kwargs['category'])
        post_data = Post.objects.order_by('-id').filter(category=category_data)
        return render(request, 'app/index.html', {
            'post_data': post_data
        })

class IndexView(TemplateView):
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
            if request.POST.get('water') == '1':
                price+=1500
        

        return render(request, 'app/price.html', {
            'form': form,
            "price":price
        })

class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/contact.html')

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

class StoreView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            start_date = date.today()
            weekday = start_date.weekday()
            # カレンダー日曜日開始
            if weekday != 6:
                start_date = start_date - timedelta(days=weekday + 1)
            return redirect('mypage', start_date.year, start_date.month, start_date.day)

        store_data = Store.objects.all()

        return render(request, 'app/store.html', {
            'store_data': store_data,
        })

class StaffView(View):
    def get(self, request, *args, **kwargs):
        store_data = get_object_or_404(Store, id=self.kwargs['pk'])
        staff_data = Staff.objects.filter(store=store_data).select_related('user')

        return render(request, 'app/staff.html', {
            'store_data': store_data,
            'staff_data': staff_data,
        })

class CalendarView(View):
    def get(self, request, *args, **kwargs):
        # staff_data = Staff.objects.filter(id=self.kwargs['pk']).select_related('user').select_related('store')[0]
        today = date.today()
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        if year and month and day:
            # 週始め
            start_date = date(year=year, month=month, day=day)
        else:
            start_date = today
        # 1週間
        days = [start_date + timedelta(days=day) for day in range(7)]
        start_day = days[0]
        end_day = days[-1]

        calendar = {}
        # 10時～20時
        for hour in range(10, 21):
            row = {}
            for day in days:
                row[day] = True
            calendar[hour] = row
        start_time = make_aware(datetime.combine(start_day, time(hour=10, minute=0, second=0)))
        end_time = make_aware(datetime.combine(end_day, time(hour=20, minute=0, second=0)))
        booking_data = Booking.objects.all().exclude(Q(start__gt=end_time) | Q(end__lt=start_time))
        for booking in booking_data:
            local_time = localtime(booking.start)
            booking_date = local_time.date()
            booking_hour = local_time.hour
            if (booking_hour in calendar) and (booking_date in calendar[booking_hour]):
                calendar[booking_hour][booking_date] = False

        return render(request, 'app/calendar.html', {
            # 'staff_data': staff_data,
            'calendar': calendar,
            'days': days,
            'start_day': start_day,
            'end_day': end_day,
            'before': days[0] - timedelta(days=7),
            'next': days[-1] + timedelta(days=1),
            'today': today,
        })

class BookingView(View):
    def get(self, request, *args, **kwargs):
        # staff_data = Staff.objects.filter(id=self.kwargs['pk']).select_related('user').select_related('store')[0]
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        hour = self.kwargs.get('hour')
        form = BookingForm(request.POST or None)

        return render(request, 'app/booking.html', {
            # 'staff_data': staff_data,
            'year': year,
            'month': month,
            'day': day,
            'hour': hour,
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        # staff_data = get_object_or_404(Staff, id=self.kwargs['pk'])
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        hour = self.kwargs.get('hour')
        start_time = make_aware(datetime(year=year, month=month, day=day, hour=hour))
        end_time = make_aware(datetime(year=year, month=month, day=day, hour=hour + 1))
        booking_data = Booking.objects.filter(start=start_time)
        form = BookingForm(request.POST or None)
        if booking_data.exists():
            form.add_error(None, '既に予約があります。\n別の日時で予約をお願いします。')
        else:
            if form.is_valid():
                booking = Booking()
                # booking.staff = staff_data
                booking.start = start_time
                booking.end = end_time
                booking.first_name = form.cleaned_data['first_name']
                booking.last_name = form.cleaned_data['last_name']
                booking.tel = form.cleaned_data['tel']
                booking.email = form.cleaned_data['email']
                booking.remarks = form.cleaned_data['remarks']
                booking.save()

                name = form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                message = form.cleaned_data['remarks']
                subject = 'お問い合わせありがとうございます。'
                content = textwrap.dedent('''
                    ※このメールはシステムからの自動返信です。
                    
                    {name} 様
                    
                    お問い合わせありがとうございました。
                    以下の内容でお問い合わせを受け付けいたしました。
                    内容を確認させていただき、ご返信させて頂きますので、少々お待ちください。
                    
                    --------------------
                    ■お名前
                    {name}
                    
                    ■メールアドレス
                    {email}
                    
                    ■メッセージ
                    {message}
                    --------------------
                    ''').format(
                        name=name,
                        email=email,
                        message=message
                    )

                to_list = [email]
                bcc_list = [settings.EMAIL_HOST_USER]

                try:
                    message = EmailMessage(subject=subject, body=content, to=to_list, bcc=bcc_list)
                    message.send()
                except BadHeaderError:
                    return HttpResponse("無効なヘッダが検出されました。")

                return redirect('thanks')

        return render(request, 'app/booking.html', {
            # 'staff_data': staff_data,
            'year': year,
            'month': month,
            'day': day,
            'hour': hour,
            'form': form,
        })



class ThanksView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/thanks.html')


class MyPageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        staff_data = Staff.objects.filter(user=request.user).select_related('user').select_related('store')[0]
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        start_date = date(year=year, month=month, day=day)
        days = [start_date + timedelta(days=day) for day in range(7)]
        start_day = days[0]
        end_day = days[-1]

        calendar = {}
        # 10時～20時
        for hour in range(10, 21):
            row = {}
            for day_ in days:
                row[day_] = ""
            calendar[hour] = row
        start_time = make_aware(datetime.combine(start_day, time(hour=10, minute=0, second=0)))
        end_time = make_aware(datetime.combine(end_day, time(hour=20, minute=0, second=0)))
        booking_data = Booking.objects.filter(staff=staff_data).exclude(Q(start__gt=end_time) | Q(end__lt=start_time))
        for booking in booking_data:
            local_time = localtime(booking.start)
            booking_date = local_time.date()
            booking_hour = local_time.hour
            if (booking_hour in calendar) and (booking_date in calendar[booking_hour]):
                calendar[booking_hour][booking_date] = booking.first_name

        return render(request, 'app/mypage.html', {
            'staff_data': staff_data,
            'booking_data': booking_data,
            'calendar': calendar,
            'days': days,
            'start_day': start_day,
            'end_day': end_day,
            'before': days[0] - timedelta(days=7),
            'next': days[-1] + timedelta(days=1),
            'year': year,
            'month': month,
            'day': day,
        })

@require_POST
def Holiday(request, year, month, day, hour):
    staff_data = Staff.objects.get(user=request.user)
    start_time = make_aware(datetime(year=year, month=month, day=day, hour=hour))
    end_time = make_aware(datetime(year=year, month=month, day=day, hour=hour + 1))

    # 休日追加
    Booking.objects.create(
        staff=staff_data,
        start=start_time,
        end=end_time,
    )

    start_date = date(year=year, month=month, day=day)
    weekday = start_date.weekday()
    # カレンダー日曜日開始
    if weekday != 6:
        start_date = start_date - timedelta(days=weekday + 1)
    return redirect('mypage', year=start_date.year, month=start_date.month, day=start_date.day)

def Delete(request, year, month, day, hour):
    start_time = make_aware(datetime(year=year, month=month, day=day, hour=hour))
    booking_data = Booking.objects.filter(start=start_time)

    # 予約削除
    booking_data.delete()

    start_date = date(year=year, month=month, day=day)
    weekday = start_date.weekday()
    # カレンダー日曜日開始
    if weekday != 6:
        start_date = start_date - timedelta(days=weekday + 1)
    return redirect('mypage', year=start_date.year, month=start_date.month, day=start_date.day)