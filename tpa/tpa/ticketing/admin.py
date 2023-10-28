from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Point)
class PointAdmin(admin.ModelAdmin):
    list_display = (
        'x',
        'y',
    )

@admin.register(models.Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = (
        'blockId',
        'blockName',
    )

@admin.register(models.Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(models.Baseball)
class BaseballAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(models.Football)
class FootballAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(models.Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = (
        'sortMapInfo',
    )
