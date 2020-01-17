from django.contrib import admin
from django.urls import re_path, path, include

urlpatterns = [
    re_path(r'^admin', admin.site.urls),
    path('', include('answers.urls')),
    path('q', include('answers.urls'))
]
