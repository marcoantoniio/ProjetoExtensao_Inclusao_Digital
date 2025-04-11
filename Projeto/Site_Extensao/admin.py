from django.contrib import admin
from django.contrib.auth.models import User
from .models import Curso

# Register your models here.

try:
    admin.site.register(User)
    admin.site.register(Curso)
except admin.sites.AlreadyRegistered:
    pass