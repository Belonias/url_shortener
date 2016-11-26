from django.contrib import admin

# Register your models here.
from .models import ClickEventManager, ClickEvent

admin.site.register(ClickEvent)
