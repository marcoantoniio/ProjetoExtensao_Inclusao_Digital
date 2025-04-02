from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.

try:
    admin.site.register(User)
except admin.sites.AlreadyRegistered:
    pass