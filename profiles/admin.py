from django.contrib import admin

# Register your models here.
from profiles.models import Member, Dependent

admin.site.register(Member)
admin.site.register(Dependent)