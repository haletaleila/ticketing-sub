from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Card)
class PointAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'isPreparing',
    )