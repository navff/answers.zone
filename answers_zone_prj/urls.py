"""answers_zone_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import re_path, path
from answers import views

urlpatterns = [
    re_path(r'^admin', admin.site.urls),
    path('q', views.QuestionsPresenter.all, name='list'),
    path('answered', views.QuestionsPresenter.answered, name='answered'),
    path('q/add', views.QuestionsPresenter.add),
    path('q/<str:question_id>', views.QuestionsPresenter.one_item),
    path('', views.QuestionsPresenter.all, name='home'),
    #question_id
]
