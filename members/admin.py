from django.contrib import admin

# Register your models here.
from .models import Member, Level

admin.site.register(Member)
admin.site.register(Level)