from django.contrib import admin
from django.urls import path
from travelplanner import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.plan_trip, name='plan_trip'),
]
