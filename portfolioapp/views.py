from django.shortcuts import render
from django.http import HttpResponse


def PortfolioHomeView(request):
    return render(request,'portfolioapp/home.html')


