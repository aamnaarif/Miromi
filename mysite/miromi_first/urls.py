from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name= 'miromi-home'),
    path('quiz/', views.quiz, name= 'miromi-quiz'),
    path('influencers/', views.influencer, name= 'miromi-influencer'),
    path('dashboard/', views.dashboard, name= 'miromi-dashboard')

]
