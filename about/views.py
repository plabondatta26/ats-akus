from django.shortcuts import render
from django.views import View


# Create your views here.

class AboutView(View):
    def get(self, request):
        return render(request, 'about/about_us.html')


class PortfolioView(View):
    def get(self, request):
        return render(request, 'about/portfolio.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'about/contact.html')
