from django.contrib import admin
from .models import Record, StreamerInfo

# Register your models here.
admin.site.register(Record)
admin.site.register(StreamerInfo)