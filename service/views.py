from django.shortcuts import render
from django.views import View


# Create your views here.
class ServiceView(View):
    def get(self, request):
        return render(request, 'service/services.html')


class BlogView(View):
    def get(self, request):
        return render(request, 'service/blogs.html')
