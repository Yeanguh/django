from django.contrib import admin

# Register your models here.
from blogs.models import Blog, Category, Tag
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)






