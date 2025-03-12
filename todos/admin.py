from django.contrib import admin
from .models import Todo

class TodoAsList(admin.ModelAdmin):
    list_display=(
        "title",
        "body",
    )

admin.site.register(Todo, TodoAsList)