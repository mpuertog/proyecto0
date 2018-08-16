from django.contrib import admin
from django.contrib.auth.models import User

from .forms import UserAdmin
from .models import Evento

# Register your models here.


admin.site.register(Evento)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
