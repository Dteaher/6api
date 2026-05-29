from django.contrib import admin

from .models import BoardGame, Category, Review


admin.site.register(Category)
admin.site.register(BoardGame)
admin.site.register(Review)
