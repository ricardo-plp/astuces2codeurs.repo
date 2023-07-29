from django.contrib import admin

# Register your models here.
from blog.models import Post



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','status','Author','created')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title','body','author')
    ordering = ('created','title','Author')