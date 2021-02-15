"""hypercar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import RedirectView
from tickets.views import WelcomeView, \
    MenuView, ChangeOilView, UpdateTiresView, DiagnosticView, ProcessingView, NextView

urlpatterns = [
    path('welcome/', WelcomeView.as_view()),
    path('menu', MenuView.as_view()),
    path('/', MenuView.as_view()),
    path('get_ticket/change_oil', ChangeOilView.as_view()),
    path('get_ticket/inflate_tires', UpdateTiresView.as_view()),
    path('get_ticket/diagnostic', DiagnosticView.as_view()),
    path('processing', ProcessingView.as_view()),
    path('processing/', RedirectView.as_view(url='processing')),
    path('next', NextView.as_view()),
    path('next/', RedirectView.as_view(url='next'))
]
