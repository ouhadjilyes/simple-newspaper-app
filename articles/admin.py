from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.admin.options import StackedInline
from .models import Article, Comment

# Register your models here.
'''class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ 
        CommentInline,
    ] '''

#another way of doing this
class CommentInline(admin.TabularInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ 
        CommentInline,
    ]
    



admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)