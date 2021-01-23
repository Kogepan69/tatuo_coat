from django.contrib import admin
from .models import Post , Category , Car , Store, Staff, Booking

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Car)
admin.site.register(Store)
admin.site.register(Staff)
admin.site.register(Booking)