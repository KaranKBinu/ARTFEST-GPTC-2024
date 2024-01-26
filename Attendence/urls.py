from django.urls import path

from Attendence import views

urlpatterns = [
    path("", views.attendence_index, name="attendence_index"),
]
