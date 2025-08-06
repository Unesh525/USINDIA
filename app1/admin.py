from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(admindata)
admin.site.register(logindata)
admin.site.register(userdata)
admin.site.register(PhishingLink)
admin.site.register(PhishedData)
