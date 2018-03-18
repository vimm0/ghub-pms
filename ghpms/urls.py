from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from app.repo.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),

]
