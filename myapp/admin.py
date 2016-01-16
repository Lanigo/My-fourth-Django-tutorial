from .models import Post, Comment  	
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ("title", "created_date")

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)  		
