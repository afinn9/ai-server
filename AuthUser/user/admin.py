from django.contrib import admin
from .models import BlacklistedToken, User

admin.site.register(BlacklistedToken)
admin.site.register(User)
