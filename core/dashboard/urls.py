from django.urls import path
from . import views
from dashboard.dash_apps.finished_apps import example


urlpatterns = [
	path('', views.homepage, name="homepage"),
	path('', views.dashboard, name="dashboard")
]