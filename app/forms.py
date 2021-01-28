from django import forms
from .models import Category


class CarForm(forms.Form):
    name = forms.CharField(max_length=100, label='車種')

class BookingForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='姓')
    last_name = forms.CharField(max_length=30, label='名')
    tel = forms.CharField(max_length=30, label='電話番号')
    address = forms.CharField(max_length=30, label='住所')
    remarks = forms.CharField(label='備考', widget=forms.Textarea())

class PostForm(forms.Form):
    category_data = Category.objects.all()
    category_choice = {}
    for category in category_data:
        category_choice[category] = category

    title = forms.CharField(max_length=50, label='タイトル')
    category = forms.ChoiceField(label='カテゴリ', widget=forms.Select, choices=list(category_choice.items())) # 追加
    content = forms.CharField(label='内容', widget=forms.Textarea())
    image = forms.ImageField(label='イメージ画像', required=False)