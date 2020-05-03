from django.contrib import admin
from .models import User, BlackListedToken

admin.site.register(User)
admin.site.register(BlackListedToken)

