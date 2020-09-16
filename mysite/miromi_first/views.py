from django.shortcuts import render
from django.http import HttpResponse
from .models import BeautyData

# Create your views here.


def landing_page(request):

    return render(request, 'miromi_first/landing_page.html')


def influencer(request):

    return render(request, 'miromi_first/influencer.html')


def dashboard(request):
    context = {
        'BeautyModels': BeautyData.objects.all
    }

    return render(request, 'miromi_first/dashboard.html', context)


def quiz(request):
    return render(request, 'miromi_first/quiz.html')
