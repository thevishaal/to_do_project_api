from django.contrib import admin
from .models import Todo

# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'status', 'priority', 'due_date')
    list_display_links = ('id', 'title')
    list_filter = ('status', 'priority', 'due_date')
    search_fields = ('title', 'description')
    ordering = ('id',)
    filter_horizontal = []