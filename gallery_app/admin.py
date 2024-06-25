from django.contrib import admin
from .models import Art_Work, UserInteraction

# Register your models here.
admin.site.register(Art_Work)
admin.site.register(UserInteraction)
