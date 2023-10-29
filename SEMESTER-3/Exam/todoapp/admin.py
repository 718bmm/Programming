from django.contrib import admin
from .models import TodoItem

# admin.site.register(Post)
@admin.register(TodoItem)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'deadline']