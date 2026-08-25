from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "text",

    )

admin.site.register(Article, ArticleAdmin)