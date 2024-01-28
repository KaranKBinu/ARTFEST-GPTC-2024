from django.urls import path

from Attendence import views

urlpatterns = [
    path("", views.attendence_index, name="attendence_index"),
    path("login", views.attendence_login, name="attendence_login"),
    path("logout/", views.attendence_logout, name="attendence_logout"),
]
