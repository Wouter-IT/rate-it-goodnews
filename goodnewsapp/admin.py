from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on', 'reported')
    list_display = ('title', 'user', 'created_on', 'reported')
    search_fields = ['title', 'content', 'user']
    summernote_fields = ('content')

   
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_filter = ('user', 'created_on', 'reported')
    list_display = ('user', 'body', 'post', 'created_on', 'reported')
    search_fields = ['user', 'body']
    summernote_fields= ('body')
