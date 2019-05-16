from django.shortcuts import render

# Create your views here.
from django.views import View

from blogs.models import Blog, Category, Tag

class IndexView(View):
    def get(self, request):
        all_blog = Blog.objects.all().order_by('-id')
        return render(request, 'index.html', {
            'all_blog': all_blog,
        })