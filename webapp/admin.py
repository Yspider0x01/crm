from django.contrib import admin
from .models import Record , Category


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    class Meta:
        list_display = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        list_display = '__all__'


