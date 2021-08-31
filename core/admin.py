from django.contrib import admin
from .models import DailyRecord, User, Habit

# Register your models here.

admin.site.register(User)
admin.site.register(DailyRecord)
admin.site.register(Habit)

