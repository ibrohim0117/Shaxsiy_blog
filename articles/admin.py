from django.contrib import admin
from .models import Article, Comments

# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comments
    extra = 0



class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comments)